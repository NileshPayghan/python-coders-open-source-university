import numpy as np
z = np.array([-5.5,2.3,1.4,-3.2,-5.3])
print(z)
z1=np.abs(z)
print(z1)
z2=np.floor(z1)
print(z2)
z3=np.copysign(z2,z)
print(z3)

"""
#OUTPUT
[-5.5  2.3  1.4 -3.2 -5.3]
[5.5 2.3 1.4 3.2 5.3]
[5. 2. 1. 3. 5.]
[-5.  2.  1. -3. -5.]
"""