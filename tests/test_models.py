"""Tests for statistics functions within the Model layer."""

import numpy as np
import pytest
import numpy.testing as npt

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4])
    ])
def test_daily_mean(test, expected):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean
   # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))



def test_daily_max_zeros():
    """  """
    from inflammation.models import daily_max

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    npt.assert_array_equal(daily_max(test_input), test_result)
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[-1, -2], [-3, -4], [-5, -6]], [-1, -2]),
    ]
)
def test_daily_max(test, expected):
    """  """
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[-1, -2], [-3, -4], [-5, -6]], [-5, -6]),
    ]
)
def test_daily_min(test, expected):
    """  """
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))
    
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])