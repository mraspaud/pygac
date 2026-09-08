"""Tests for reading pygac's settings."""

from pygac.configuration import get_config, read_config_file, reset_config


def test_settings_can_be_put_back_the_way_they_were_found(tmp_path):
    """Reading settings changes the process, and a caller must be able to undo that."""
    settings = tmp_path / "pygac.cfg"
    settings.write_text("[scan_angles]\nnoaa19 = 55.301\n")
    read_config_file(str(settings))

    reset_config()

    assert not get_config(initialized=False).sections()
