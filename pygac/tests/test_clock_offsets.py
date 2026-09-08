"""Tests for the tables of measured spacecraft clock error."""

import numpy as np

from pygac.clock_offsets_converter import clock_table_covers


def test_a_time_inside_a_measured_segment_is_covered():
    """NOAA-9's table was measured across 1993, so a pass from then is not guesswork."""
    assert clock_table_covers("noaa9", np.datetime64("1993-06-01T12:00:00"))


def test_a_platform_with_no_table_is_covered_nowhere():
    """noaa10 has no measured clock error at all, so nothing about it is known."""
    assert not clock_table_covers("noaa10", np.datetime64("1988-05-15T09:00:00"))


def test_a_moment_past_the_end_of_a_table_is_not_covered():
    """noaa9's measurements stop in August 1995; after that nothing was recorded."""
    assert not clock_table_covers("noaa9", np.datetime64("1998-06-01T00:00:00"))
