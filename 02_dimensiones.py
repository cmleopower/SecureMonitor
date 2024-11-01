import numpy as np # type: ignore
import pandas as pd # type: ignore

# Crear un array de 1 dimensión
data = np.array([1, 2, 3, 4, 5])
s = pd.Series(data)
print(s)
print(type(s))

#vector

vector =np.array([1,2,3,4,5])
print(vector)
print(type(vector))

# vector de 2 dimensiones
# cada corchete representa una dimensión
vector2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(vector2)
print(type(vector2))

# tensor de 3 dimensiones
# cada corchete representa una dimensión

tensor = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(tensor)
print(type(tensor))

array_arage = np.arange(1,10)
print(array_arage)

eye_matrix = np.eye(3)
print(eye_matrix)


random_matrix = np.random.random((2,2))
print(random_matrix)
