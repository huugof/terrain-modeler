# Output Resolution, Multi-User Build Behavior, and Contour Smoothing

This review is based on the current code paths in `src/` and the corresponding tests in `tests/`.

## 1) How "Output Resolution" works today

Short answer: in the web UI, the **Output Resolution slider does not change LiDAR rasterization resolution**. It changes **terrain mesh sampling density** after the raster already exists.

### Exact execution order

1. Point cloud (LAZ/EPT subset) is rasterized into DTM/DSM at `cfg.resolution` (`make_dtm`, `make_dsm`).
2. Terrain mesh is then created from the DTM raster using `sample=cfg.terrain_sample`.

So reduction happens in two places conceptually:
- LiDAR -> raster aggregation (always happens).
- Raster -> terrain mesh decimation (what the web slider controls).

### What the slider maps to

Web form slider:
- `terrain_complexity` is integer `0..10`.
- Backend maps it with: `terrain_sample = max(1, 11 - terrain_complexity)`.

So:
- Higher complexity => lower sample step => denser mesh.
- Lower complexity => higher sample step => sparser mesh.

### Quantifiable reduction from slider

Relative to `terrain_sample=1` mesh (same DTM), mesh point/face density scales approximately as:

`retained_density ~= 1 / terrain_sample^2`

Mapping:

| UI value (`terrain_complexity`) | `terrain_sample` | Approx retained terrain mesh density vs sample=1 |
|---|---:|---:|
| 10 | 1  | 100% |
| 9  | 2  | 25.00% |
| 8  | 3  | 11.11% |
| 7  | 4  | 6.25% |
| 6  | 5  | 4.00% |
| 5 (default) | 6 | 2.78% |
| 4  | 7  | 2.04% |
| 3  | 8  | 1.56% |
| 2  | 9  | 1.23% |
| 1  | 10 | 1.00% |
| 0  | 11 | 0.83% |

### Does it reduce points first, then mesh, or mesh then reduce?

For web slider behavior: neither exactly. It reduces the **raster sampling used to build the mesh** (not raw point-cloud point count).

### Can we state points/m² from the slider?

Not as source LiDAR points/m². That depends on incoming dataset density and coverage.

What we can state consistently:
- **Mesh vertex spacing** (approx) = `DTM_cell_size * terrain_sample`.
- **Mesh vertex density** (approx) = `1 / (DTM_cell_size * terrain_sample)^2`.

In web mode, `DTM_cell_size` is fixed to `DEFAULT_RESOLUTION` (currently `1.0` in LAZ CRS units), and the slider only changes `terrain_sample`.

Also note: CLI has a separate `--resolution` (true raster cell size control), but web UI currently does not expose it.

## 2) What happens with multiple simultaneous builds

### Current behavior

- Each `/run` request creates a `Job` and starts a **new daemon thread** to execute `_run_build_job`.
- There is no global queue/worker pool in-process.

### Limits currently applied

When auth is enabled:
- Hourly and daily request limits per user.
- Active job limit per user (`MAX_ACTIVE_JOBS_PER_USER`, default `1`).

When auth is disabled (desktop mode path):
- No per-user build throttling is applied.

### Important concurrency implications

1. **No global concurrency cap**
- Multiple users can run builds concurrently (subject only to per-user limits).
- Heavy concurrent builds can saturate CPU/RAM/disk/network.

2. **Per-user active-job check is not transactional**
- The check and the `set_active_job` write are separate operations.
- Two near-simultaneous requests from one user can race and both pass before either is marked active.

3. **Multi-process deployment caveat (major)**
- Job state (`JOBS`, logs, recent-jobs cache) is in-memory per process.
- Gunicorn is configured with multiple workers (`workers = 2`).
- That means requests hitting different workers can see inconsistent in-memory job visibility/log streaming unless they happen to land on the same worker process.
- SQLite persistence helps history/rehydration but is not a real-time cross-worker event bus.

## 3) How contour smoothing works and how to express it

Short answer: this is **resampling**, not geometric smoothing/splining.

### Actual flow

1. Contours are generated from the terrain raster (`generate_contours_from_raster`) at the selected contour interval.
2. For DXF export, if `dxf_contour_spacing > 0`, each contour polyline is resampled at uniform XY spacing (`resample_contours` -> `_resample_polyline`).
3. If spacing is `0`/unset, original contour vertices are kept.

### Consistent metric you can communicate

Yes: use **vertex spacing along contour line** in current output units.

If spacing is `s`:
- Approx vertices per linear unit = `1 / s`.
- In feet mode: points per foot along contour ~ `1 / s`.
- In meters mode: points per meter along contour ~ `1 / s`.

Examples (feet mode):
- `s=1` => ~1 point/ft
- `s=2` => ~0.5 points/ft
- `s=5` => ~0.2 points/ft
- `s=10` => ~0.1 points/ft

At `0`: no fixed points/ft metric, because you keep raw contour extraction vertices (depends on raster topology and contour geometry).

### Repeatability guidance

To keep contour output repeatable, keep all of these fixed:
- Units (`feet`/`meters`)
- Contour interval
- Contour spacing (`dxf_contour_spacing`)
- Input data source / clip area
- DTM resolution and terrain preprocessing settings

## Code references

- UI slider definitions: `src/va_lidar_context/templates/index.html:228`, `src/va_lidar_context/templates/index.html:263`
- Web mapping `terrain_complexity -> terrain_sample`: `src/va_lidar_context/webapp/routes.py:625`
- Web keeps raster resolution at default: `src/va_lidar_context/webapp/routes.py:624`
- DTM/DSM use `cfg.resolution`: `src/va_lidar_context/pipeline/build.py:748`, `src/va_lidar_context/pipeline/build.py:766`, `src/va_lidar_context/core/raster.py:93`
- Terrain mesh decimation uses `sample`: `src/va_lidar_context/pipeline/build.py:1255`, `src/va_lidar_context/core/mesh.py:157`
- CLI exposes true `--resolution`: `src/va_lidar_context/cli.py:106`
- Contour generation and resampling: `src/va_lidar_context/pipeline/build.py:1386`, `src/va_lidar_context/pipeline/build.py:930`, `src/va_lidar_context/core/mesh.py:344`, `src/va_lidar_context/core/mesh.py:438`, `src/va_lidar_context/core/mesh.py:495`
- Build request starts thread per job: `src/va_lidar_context/webapp/routes.py:816`
- In-memory per-process job store: `src/va_lidar_context/webapp/jobs.py:55`
- Recent jobs read from in-memory `JOBS`: `src/va_lidar_context/webapp/jobs.py:459`
- Snapshot persistence / rehydrate: `src/va_lidar_context/webapp/jobs.py:323`, `src/va_lidar_context/webapp/jobs.py:424`
- Per-user rate/active-job limits: `src/va_lidar_context/webapp/auth.py:165`, `src/va_lidar_context/auth_store.py:560`, `src/va_lidar_context/webapp/settings.py:126`
- Desktop mode note (no per-user build throttling): `src/va_lidar_context/webapp/routes.py:589`
- Gunicorn multi-worker config: `gunicorn.conf.py:2`
