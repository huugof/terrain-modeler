use std::{
    io,
    net::TcpStream,
    path::PathBuf,
    sync::Mutex,
    thread,
    time::{Duration, Instant},
};

use tauri::{AppHandle, Manager};
use tauri_plugin_shell::{process::CommandChild, ShellExt};

const SIDECAR_NAME: &str = "terrain-modeler-backend";
const BACKEND_URL: &str = "http://127.0.0.1:8000/";
const BACKEND_HOST_PORT: &str = "127.0.0.1:8000";

struct SidecarState(Mutex<Option<CommandChild>>);

fn default_out_dir() -> PathBuf {
    if let Some(home) = std::env::var_os("HOME") {
        let mut path = PathBuf::from(home);
        path.push("Documents");
        path.push("TerrainModeler");
        return path;
    }
    PathBuf::from("./out")
}

fn wait_for_backend(timeout: Duration) -> Result<(), String> {
    let started = Instant::now();
    while started.elapsed() < timeout {
        if TcpStream::connect(BACKEND_HOST_PORT).is_ok() {
            return Ok(());
        }
        thread::sleep(Duration::from_millis(250));
    }
    Err(format!(
        "Backend did not start within {}s",
        timeout.as_secs()
    ))
}

fn stop_sidecar(app: &AppHandle) {
    if let Some(state) = app.try_state::<SidecarState>() {
        if let Ok(mut guard) = state.0.lock() {
            if let Some(child) = guard.take() {
                let _ = child.kill();
            }
        }
    }
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .setup(|app| {
            let out_dir = std::env::var("VA_OUT_DIR")
                .map(PathBuf::from)
                .unwrap_or_else(|_| default_out_dir());

            let sidecar = app
                .shell()
                .sidecar(SIDECAR_NAME)?
                .env("VA_DESKTOP_MODE", "1")
                .env("VA_OUT_DIR", out_dir.to_string_lossy().to_string())
                .env("VA_RETENTION_DAYS", "0")
                .args(["--host", "127.0.0.1", "--port", "8000"]);

            let (_receiver, child) = sidecar.spawn()?;
            app.manage(SidecarState(Mutex::new(Some(child))));

            wait_for_backend(Duration::from_secs(25)).map_err(io::Error::other)?;

            if let Some(window) = app.get_webview_window("main") {
                let js = format!("window.location.replace('{}');", BACKEND_URL);
                let _ = window.eval(&js);
            }
            Ok(())
        })
        .build(tauri::generate_context!())
        .expect("error building terrain-modeler shell")
        .run(|app_handle, event| {
            if let tauri::RunEvent::ExitRequested { .. } = event {
                stop_sidecar(app_handle);
            }
        })
}
