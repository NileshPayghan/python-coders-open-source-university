import numpy as np

print(f'{"-"*50}')
print(f'np arange: {np.arange(4)}')
print(f'one plus np arange: {1 + np.arange(4)}')
print(f'{"-"*50}')
z = np.diag(1 + np.arange(4), k=0)
print(z)
print(f'{"-"*50}')

"""
#OUTPUT
--------------------------------------------------
np arange: [0 1 2 3]
one plus np arange: [1 2 3 4]
--------------------------------------------------
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
--------------------------------------------------

"""
