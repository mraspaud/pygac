"""Tests for the tables of measured spacecraft clock error."""

import numpy as np
import pytest

from pygac.clock_offsets_converter import clock_measurements_reach, get_offsets, txt


def test_measurements_reach_a_time_inside_them():
    """NOAA-9's table was measured across 1993, so a pass from then is not guesswork."""
    assert clock_measurements_reach("noaa9", np.datetime64("1993-06-01T12:00:00"))


def test_a_platform_with_no_table_reaches_nothing():
    """noaa10 has no measured clock error at all, so nothing about it is known."""
    assert not clock_measurements_reach("noaa10", np.datetime64("1988-05-15T09:00:00"))


def test_measurements_do_not_reach_past_the_end_of_a_table():
    """noaa9's measurements stop in August 1995; after that nothing was recorded."""
    assert not clock_measurements_reach("noaa9", np.datetime64("1998-06-01T00:00:00"))


def test_every_table_runs_forwards_in_time():
    """np.interp needs its points in order; given them out of order it returns nonsense."""
    for spacecraft_name in sorted(txt):
        measured, _ = get_offsets(spacecraft_name)
        backwards = [(a, b) for a, b in zip(measured, measured[1:]) if b < a]
        assert not backwards, f"{spacecraft_name} steps backwards at {backwards[:1]}"


def test_a_table_that_has_lost_a_measurement_is_refused(monkeypatch):
    """These tables are edited by hand, and a dropped line changes navigation silently."""
    monkeypatch.setitem(txt, "noaa9", "\n".join(txt["noaa9"].strip().split("\n")[:-1]))
    with pytest.raises(ValueError, match="measurement"):
        get_offsets("noaa9")
