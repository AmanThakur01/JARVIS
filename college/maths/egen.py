import numpy as np

a = np.array([[3, 1], [2, 2]])
w, v = np.linalg.eig(a)

print("value:",w)
print("vector:",v)

