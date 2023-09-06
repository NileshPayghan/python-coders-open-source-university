'''
Create random vector size and sort it.
'''

import numpy as np

z = np.random.random(10)
z.sort()  # inplace sorting
print(z)


'''
Output:
[0.02500063 0.04542524 0.18915105 0.26321673 0.34361825 0.40474406
 0.52903861 0.65446214 0.86329856 0.98644956]
'''