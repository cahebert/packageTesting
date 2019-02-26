from darkbox import energy
from numpy.testing import assert_equal
import numpy as np

def test_abs_area():
    y = energy.abs_area(np.array([1,2,3]))
    assert_equal(y,6)

