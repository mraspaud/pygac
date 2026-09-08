"""Tests for the tables of measured spacecraft clock error."""

import numpy as np

from pygac.clock_offsets_converter import clock_table_covers


def test_a_time_inside_a_measured_segment_is_covered():
    """NOAA-9's table was measured across 1993, so a pass from then is not guesswork."""
    assert clock_table_covers("noaa9", np.datetime64("1993-06-01T12:00:00"))
