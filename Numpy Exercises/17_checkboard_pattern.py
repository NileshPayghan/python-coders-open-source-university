import numpy as np

row_col = 12
z = np.zeros((row_col,row_col), dtype=int)
print(f'zeros with int:\n{z}')

z[1::2,::2] = 1
z[::2,1::2] = 1
print(f'Updated pattern:\n{z}')