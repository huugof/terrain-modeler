from va_lidar_context.webapp.forms import snapshot_defaults


def test_snapshot_defaults_use_grand_canyon_seed_values():
    defaults = snapshot_defaults()
    assert defaults["provider"] == "national"
    assert defaults["provider_label"] == "USGS 3DEP (National)"
    assert defaults["center1"] == 36.09841234052352
    assert defaults["center2"] == -112.0952885242688
    assert defaults["clip_size"] == 3000.0
    assert defaults["output_naip"] is True
