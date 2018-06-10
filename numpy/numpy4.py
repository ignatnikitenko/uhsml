import numpy as np

A = np.eye(3)
B = np.eye(3)
print(A)
print(B)

AB = np.hstack((A, B))
print(AB)
