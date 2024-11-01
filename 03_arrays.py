import numpy as np # type: ignore
import pandas as pd # type: ignore

# Crear un array de 4 dimensiones
# cada corchete representa una dimensión

array = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)
print(array)

z = np.array(3, dtype='uint8')
print(z)

double_array = np.array([1,2,3,4,5], dtype='float64')
print(double_array)

