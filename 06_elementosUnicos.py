import numpy as np # type: ignore
import pandas as pd # type: ignore

# Elementos únicos
# La función unique() devuelve los elementos únicos de un array.

array = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
unique = np.unique(array)
print(unique)

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]])
unique2 = np.unique(array2)
print(unique2)