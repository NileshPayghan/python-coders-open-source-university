'''
Build Array using generators
'''

import numpy as np


def generate():
    for x in range(10):
        yield x


z = np.fromiter(generate(), dtype=int, count=-1)
print(z)

'''
Output:
[0 1 2 3 4 5 6 7 8 9]
'''