import numpy as np # type: ignore
import pandas as pd # type: ignore

matrix = np.array([[1,2,3,4,5],[6,7,8,9,10]])
transposed_matrix = matrix.T
print(transposed_matrix)

array = np.arange(1,10)
reshaped_array = array.reshape(3,3)
print(reshaped_array)

reversed_array = np.flip(array)
print(reversed_array)
