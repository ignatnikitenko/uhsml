import numpy as np

m = np.mean(matrix, axis=0)
std = np.std(matrix, axis=0)
matrix_norm = ((matrix - m) / std)
print(matrix_norm)
