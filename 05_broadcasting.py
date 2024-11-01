import numpy as np # type: ignore
import pandas as pd # type: ignore

# Broadcasting
# Broadcasting es una técnica que permite realizar operaciones entre arrays de diferentes tamaños.

prices = np.array([100, 200, 300, 400, 500])
discount = np.array ([0.9])
discounted_prices = prices * discount
print(discounted_prices)

prices2 = np.random.randint(100, 500, size=(5))
discount2 = np.array([0.9])
discounted_prices = prices2 + discount2
print(discounted_prices)

array = np.array([1, 2, 3, 4, 5])
print(np.all(array > 1))

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
array3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
concatenated = np.concatenate((array2, array2), axis=0)
print(concatenated)

#stacking
stacked = np.stack((array2, array2), axis=0)
print(stacked)