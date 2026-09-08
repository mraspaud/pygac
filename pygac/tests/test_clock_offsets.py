"""Tests for the tables of measured spacecraft clock error."""

import numpy as np

from pygac.clock_offsets_converter import clock_measurements_reach


def test_measurements_reach_a_time_inside_them():
    """NOAA-9's table was measured across 1993, so a pass from then is not guesswork."""
    assert clock_measurements_reach("noaa9", np.datetime64("1993-06-01T12:00:00"))


def test_a_platform_with_no_table_reaches_nothing():
    """noaa10 has no measured clock error at all, so nothing about it is known."""
    assert not clock_measurements_reach("noaa10", np.datetime64("1988-05-15T09:00:00"))


def test_measurements_do_not_reach_past_the_end_of_a_table():
    """noaa9's measurements stop in August 1995; after that nothing was recorded."""
    assert not clock_measurements_reach("noaa9", np.datetime64("1998-06-01T00:00:00"))
