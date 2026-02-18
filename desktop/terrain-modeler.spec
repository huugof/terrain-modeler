# -*- mode: python ; coding: utf-8 -*-
from __future__ import annotations

import os
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files

ROOT = Path(SPECPATH).resolve().parent if "SPECPATH" in globals() else Path(os.getcwd())

entry_script = ROOT / "desktop" / "sidecar_entry.py"

datas = []
datas += collect_data_files("pyproj")
datas += [
    (str(ROOT / "src" / "va_lidar_context" / "templates"), "va_lidar_context/templates"),
    (str(ROOT / "src" / "va_lidar_context" / "static"), "va_lidar_context/static"),
    (
        str(ROOT / "src" / "va_lidar_context" / "parcels" / "sources.json"),
        "va_lidar_context/parcels",
    ),
]

hiddenimports = [
    "mapbox_earcut",
    "trimesh.exchange.obj",
]

block_cipher = None

a = Analysis(
    [str(entry_script)],
    pathex=[str(ROOT / "src")],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="terrain-modeler-backend",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    argv_emulation=False,
    codesign_identity=None,
    entitlements_file=None,
)
