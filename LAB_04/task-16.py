# მოახდინეთ ორი ვექტორის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)

import numpy as np

matrix1 = np.array([[3, 5, 7], [3, 4, 5, ], [8, 5, 4]])
matrix2 = np.array([[3, 5, 7], [3, 4, 5, ], [8, 5, 4]])

print("Static Matrix Mult: ")
print(matrix1.dot(matrix2))

matrix_3 = np.random.randint(1, 100, size=(4, 4))
matrix_4 = np.random.randint(1, 100, size=(4, 4))
print("Random Matrix Mult: ")
print(matrix_3.dot(matrix_4))
