from numpy import array
# from scipy import *
from scipy.linalg import funm
m = array([[5, -2], [1, 2]])
funm(m, lambda x: x**2 - 7*x + 12)