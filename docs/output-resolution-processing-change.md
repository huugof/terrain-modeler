# Output Resolution Processing Change

## What Changed

The web slider now controls terrain detail upstream (raster generation) instead of only downstream (mesh/XYZ sampling), behind:

- `WEB_UPSTREAM_TERRAIN_RESOLUTION=1` (default on)

Route mapping in `src/va_lidar_context/webapp/routes.py`:

- `terrain_sample_legacy = _terrain_complexity_to_reduction(terrain_complexity)`
- Web slider map (`0..10` -> reduction factor):
  - `0->25`, `1->20`, `2->15`, `3->11`, `4->8`, `5->6`, `6->5`, `7->4`, `8->3`, `9->2`, `10->1`
- Upstream mode:
  - `terrain_resolution = resolution * terrain_sample_legacy`
  - `terrain_sample = 1`
- Legacy mode (`WEB_UPSTREAM_TERRAIN_RESOLUTION=0`):
  - `terrain_resolution = None`
  - `terrain_sample = terrain_sample_legacy`

## New Raster Processing Order

Pipeline updates in `src/va_lidar_context/pipeline/build.py`:

1. Build base DTM at `cfg.resolution` (`dtm.tif`) for heights/contours.
2. Optional DTM fill on base DTM (`dtm_filled.tif`) for heights/contours.
3. Building heights still use high-resolution DTM + nDSM path.
4. If `cfg.terrain_resolution > cfg.resolution`, build separate coarse terrain DTM:
   - `dtm_terrain.tif`
   - optional `dtm_terrain_filled.tif`
5. Clip sources separately when clipping is enabled:
   - Contours: high-res source (`dtm_clip.tif` or `dtm_contour_clip.tif`)
   - Terrain mesh / XYZ grid: coarse source (`dtm_terrain_clip.tif`) when enabled

Contour generation now always reads the contour source path (high-res), not the terrain mesh source path.

## Quantification Metric

`report.json` now includes `terrain_processing` with:

- `base_cell_size`
- `terrain_raster_cell_size`
- `mesh_sample_step`
- `effective_mesh_cell_size`
- `upstream_resolution_enabled`
- `estimated_vertex_ratio_vs_base`
- `estimated_vertex_reduction_percent`

Formulas:

- `effective_mesh_cell_size = terrain_raster_cell_size * mesh_sample_step`
- `estimated_vertex_ratio_vs_base = (base_cell_size / effective_mesh_cell_size)^2`
- `estimated_vertex_reduction_percent = max(0, (1 - ratio) * 100)`

This gives a consistent, reportable estimate of terrain vertex density reduction versus the base DTM.

## Validation Added

- `tests/test_parse_inputs.py`
  - verifies slider mapping in upstream and legacy modes
- `tests/test_terrain_resolution_pipeline.py`
  - verifies raster-source selection and clip behavior in upstream and legacy modes
