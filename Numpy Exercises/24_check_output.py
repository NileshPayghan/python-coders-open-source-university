# What is the output of the following script?

print(f'range {list(range(5))}')
print(sum(range(5),-1)) # sum of range values in reverse way.

from numpy import *

print(f'range {list(range(5))}')
print(sum(range(5), -1))

"""
#OUTPUT
range [0, 1, 2, 3, 4]
9
range [0, 1, 2, 3, 4]
10

"""