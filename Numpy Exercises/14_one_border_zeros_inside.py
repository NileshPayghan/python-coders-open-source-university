import numpy as np

z = np.ones((10,10))
print(f'{"-"*50}')
print(f'Matrix with Ones: {z}')
print(f'{"-"*50}')
z[1:-1,1:-1] = 0
print(f'Updated z inside zeros and at border ones: {z}')