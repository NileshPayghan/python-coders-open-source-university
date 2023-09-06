'''
Sum small array faster than np.sum method
'''
import numpy as np

z = np.arange(10)
total = np.add.reduce(z)
print(total)

'''
Output:
45
'''