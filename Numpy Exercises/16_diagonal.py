import numpy as np

print(f'{"-"*50}')
print(f'np arange: {np.arange(4)}')
print(f'one plus np arange: {1 + np.arange(4)}')
print(f'{"-"*50}')
z = np.diag(1 + np.arange(4), k=0)
print(z)
print(f'{"-"*50}')
