import numpy as np
# import math
a = np.array([[8,-6,2],[-6,7,-4],[2,-4,3]])
w, v = np.linalg.eig(a)

print("value:",w)
print("vector:",v)

