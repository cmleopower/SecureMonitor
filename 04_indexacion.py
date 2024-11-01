import numpy as np # type: ignore
import pandas as pd # type: ignore

# La indexación y Slicing permiten seleccionar elementos de un array.

# Indexación
# La indexación en arrays de numpy es similar a la indexación en listas de python.
# En arrays de 1 dimensión, la indexación es similar a las listas de python.

array = np.array([1, 2, 3, 4, 5])
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])

# En arrays de 2 dimensiones, la indexación es similar a las listas de listas de python.

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array2[0][0])
print(array2[0][1])
print(array2[0][2])
print(array2[0][3])
print(array2[0][4])
print(array2[1][0])
print(array2[1][1])
print(array2[1][2])
print(array2[1][3])
print(array2[1][4])

# En arrays de 3 dimensiones, la indexación es similar a las listas de listas de listas de python.

array3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
print(array3[0][0][0])
print(array3[0][0][1])
print(array3[0][0][2])
print(array3[0][0][3])
print(array3[0][0][4])
print(array3[0][1][0])
print(array3[0][1][1])
print(array3[0][1][2])
print(array3[0][1][3])
print(array3[0][1][4])
print(array3[1][0][0])
print(array3[1][0][1])
print(array3[1][0][2])
print(array3[1][0][3])
print(array3[1][0][4])


# Slicing
# El slicing en arrays de numpy es similar al slicing en listas de python.
# En arrays de 1 dimensión, el slicing es similar a las listas de python.

array = np.array([1, 2, 3, 4, 5])
print(array[0:2])
print(array[1:3])
print(array[2:4])
print(array[3:5])
print(array[0:5])


# En arrays de 2 dimensiones, el slicing es similar a las listas de listas de python.

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array2[0:1, 0:2])
print(array2[0:1, 1:3])
print(array2[0:1, 2:4])
print(array2[0:1, 3:5])
print(array2[1:2, 0:2])
print(array2[1:2, 1:3])
print(array2[1:2, 2:4])
print(array2[1:2, 3:5])


# En arrays de 3 dimensiones, el slicing es similar a las listas de listas de listas de python.

array3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(array3[0:1, 0:1, 0:2])
print(array3[0:1, 0:1, 1:3])
print(array3[0:1, 0:1, 2:4])
print(array3[0:1, 0:1, 3:5])
print(array3[0:1, 1:2, 0:2])
print(array3[0:1, 1:2, 1:3])
print(array3[0:1, 1:2, 2:4])
print(array3[0:1, 1:2, 3:5])
print(array3[1:2, 0:1, 0:2])
print(array3[1:2, 0:1, 1:3])
print(array3[1:2, 0:1, 2:4])
print(array3[1:2, 0:1, 3:5])
print(array3[1:2, 1:2, 0:2])
print(array3[1:2, 1:2, 1:3])