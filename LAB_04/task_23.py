# შეავსეთ ორი 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. გადაიყვანეთ
# ორივე მატრიცა ერთ ლისტად. გამოიყენეთ numpy ბიბლიოთეკა.

import numpy as np

matrix1 = np.random.randint(0, 10, size=(10, 10))
print("Matrix #1: ")
print(matrix1)

matrix2 = np.random.randint(0, 10, size=(10, 10))
print("Matrix #2: ")
print(matrix2)

mergedMatrix = np.block([[matrix1, matrix2]])
print("Matrices Merged: ")
print(mergedMatrix)
