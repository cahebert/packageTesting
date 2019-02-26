import numpy as np

def abs_area(x):
    '''
    Computes the absolute area of an input array x.

    Parameters
    ----------
    x : nparray
        The array to calculate the area of

    Returns
    -------
    abs_area : the caluclated area
    '''
    return np.sum(abs(x))
