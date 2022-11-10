# შეავსეთ 3x3 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. გამოიყენეთ numpy
# ბიბლიოთეკა.

import numpy as np


matrix_3 = np.random.randint(0, 10, size=(3, 3))
matrix_4 = np.random.randint(0, 10, size=(3, 3))
print("Random Matrix Mult: ")
print(matrix_3.dot(matrix_4))
