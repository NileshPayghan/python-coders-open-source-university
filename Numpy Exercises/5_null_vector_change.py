import numpy as np

zeros_np = np.zeros(10)
print(f'{"-"*50}')
print(f'Create values with Zeros using numpy using np.zeros(10): {zeros_np}')
zeros_np[4] = 1
print(f'Change fifth element: {zeros_np}')
print(f'{"-"*50}')