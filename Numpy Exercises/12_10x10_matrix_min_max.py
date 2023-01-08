import numpy as np

z = np.random.random((10,10))

min_z, max_z = z.min(), z.max()

print(f'10x10 Matrix: {z}')
print(f'Min and Max Values 10x10 matrix Min: {min_z}, Max: {max_z}')
