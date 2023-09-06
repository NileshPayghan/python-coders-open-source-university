'''
Create a 5x5 matrix with row values ranging from 0 to 4
'''
import numpy as np

z = np.zeros((5, 5))
z += np.arange(5)
print(z)

'''
Output:
[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]
'''