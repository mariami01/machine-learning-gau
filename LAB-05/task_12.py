# find det
import numpy as np

# 2D array
a = np.array([[1, 2], [3, 4]])
det_a = np.linalg.det(a)


# 3D array
a1 = np.array([
    [1, 4, 2], 
    [3, 5, 4], 
    [3, 4,5]
    ])

det_a1 = np.linalg.det(a1)
print(det_a)
print(det_a1)