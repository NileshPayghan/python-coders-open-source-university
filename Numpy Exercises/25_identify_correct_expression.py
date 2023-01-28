import numpy as np

z=np.arange(10)
print(z**z)
print(2 << z >> 2)
print(z <- z)
print(1j*z)
print(z/1/1)
print(z<z<z) # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()


"""
#OUTPUT
[        1         1         4        27       256      3125     46656
    823543  16777216 387420489]
[  0   1   2   4   8  16  32  64 128 256]
[False False False False False False False False False False]
[0.+0.j 0.+1.j 0.+2.j 0.+3.j 0.+4.j 0.+5.j 0.+6.j 0.+7.j 0.+8.j 0.+9.j]
[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
Traceback (most recent call last):
  File "/home/trigen/Documents/Nilesh/Practice/python-coders-open-source-university/Numpy Exercises/25_identify_correct_expression.py", line 9, in <module>
    print(z<z<z)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

"""