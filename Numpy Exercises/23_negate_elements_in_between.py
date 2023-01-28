# Given a 1D array, negate all elements which are between 3 and 8, in place.
import numpy as np

z = np.arange(11)

print(f'{z=}')

z[(3<z) & (z<=8)] *= -1

print(f'{z=}')

"""
#OUTPUT
z=array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
z=array([ 0,  1,  2,  3, -4, -5, -6, -7, -8,  9, 10])

"""