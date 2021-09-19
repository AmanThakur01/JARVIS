import numpy as np

# If a system has at least one solution, it is said to be consistent .
# If a consistent system has exactly one solution, it is independent .
# If a consistent system has an infinite number of solutions, it is dependent .
# When you graph the equations, both equations represent the same line.

# _______________________________________________________________for 2 equations
# 4x  + 3y = 20
# -5x + 9y = 26


A1 = np.array([[4, 3],
              [-5, 9]])

B1 = np.array([20, 26])
X2 = np.linalg.inv(A1).dot(B1)
print("A1&B1 = ",X2)

# ___________________________________________________________________for 3 equations
A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X3 = np.linalg.inv(A).dot(B)

print("A&B=",X3)

s=np.square(A)
print("sqr= ",s)
