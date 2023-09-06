import numpy as np

print(np.array(0) / np.array(0))
print(np.array(0) / np.array(0.))
print(np.array(0) // np.array(0))
print(np.array(0) // np.array(0.))
print(np.array([np.nan]).astype(int).astype(float))

"""
#OUTPUT
26_result_of_expressions.py:3: RuntimeWarning: divide by zero encountered in floor_divide
  print(np.array(0) // np.array(0))
0
26_result_of_expressions.py:3: RuntimeWarning: invalid value encountered in divide
  print(np.array(0) / np.array(0))
nan
26_result_of_expressions.py:4: RuntimeWarning: divide by zero encountered in floor_divide
  print(np.array(0) // np.array(0))
0
[-9.22337204e+18]
"""










