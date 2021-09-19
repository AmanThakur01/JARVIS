import numpy as np

mtx = np.array([[1, 2, 1],
                [3, 4, 7],
                [3, 6, 3]])

rank = np.linalg.matrix_rank(mtx)
print("Rank of the given Matrix is : ", rank)
