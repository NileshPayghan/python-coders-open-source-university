import numpy as np
list1 = [1,2,0,0,4,0]

print(f'{"-"*50}')
print(f'List with zeros {list1}')
print(f'Indices without zero elements: {np.nonzero(list1)}')
print(f'{"-"*50}')

"""
#OUTPUT
--------------------------------------------------
List with zeros [1, 2, 0, 0, 4, 0]
Indices without zero elements: (array([0, 1, 4]),)
--------------------------------------------------

"""