# Normalize a 5x5 random matrix
import numpy as np

z = np.random.random((5,5))
zmax, zmin = z.max(), z.min()
z = (z - zmin) / (zmax - zmin)
print(z)

