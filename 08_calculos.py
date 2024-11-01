import numpy as np # type: ignore
import pandas as pd # type: ignore

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

#suma
suma = A + B
print(suma)

#resta
resta = A - B
print(resta)

#multiplicación
multiplicacion = A * B
print(multiplicacion)

#división
division = A / B
print(division)

#multiplicación de matrices
multiplicacion_matrices = A.dot(B)
print(multiplicacion_matrices)

