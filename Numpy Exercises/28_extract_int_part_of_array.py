'''
Extract the integer part of a random array using 5 different methods
'''

import numpy as np
z = np.random.uniform(0, 10, 10)

print(z - z % 1)
print(np.floor(z))
print(np.ceil(z))
print(z.astype(int))
print(np.trunc(z))


'''
Output:
[0. 1. 7. 9. 7. 4. 8. 2. 6. 3.]
[0. 1. 7. 9. 7. 4. 8. 2. 6. 3.]
[ 1.  2.  8. 10.  8.  5.  9.  3.  7.  4.]
[0 1 7 9 7 4 8 2 6 3]
[0. 1. 7. 9. 7. 4. 8. 2. 6. 3.]

'''
