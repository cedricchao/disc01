from numpy import genfromtxt
import numpy as np
import os

def data2array(filepath):
    """
    data2array takes in the filepath of a 
    data file like `restaurant.csv` in 
    data directory, and returns a 1d array
    of data.

    :Example:
    >>> fp = os.path.join('data', 'restaurant.csv')
    >>> arr = data2array(fp)
    >>> isinstance(arr, np.ndarray)
    True
    >>> arr.dtype == np.dtype('float64')
    True
    >>> arr.shape[0]
    100000
    """
    my_data = genfromtxt('data/restaurant.csv', delimiter=',',dtype = float)[1:]
    return my_data


def ends_in_9(arr):
    """
    ends_in_9 takes in an array of dollar amounts 
    and returns the proprtion of values that end 
    in 9 in the hundredths place.

    :Example:
    >>> arr = np.array([23.04, 45.00, 0.50, 0.09])
    >>> out = ends_in_9(arr)
    >>> 0 <= out <= 1
    True
    """
    num1 = np.count_nonzero(arr)
    my_data1 = arr*100
    my_data2 = map(lambda x: round(x), my_data1)
    try1 = map(lambda x: x%10==9, my_data2)
    count = list(try1).count(True)
    count
    proportion = count/num1
    return proportion
