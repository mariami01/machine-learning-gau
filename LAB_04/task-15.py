# მოახდინეთ ორი მატრიცის შეკრების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)

import numpy as np

matrix1 = np.array([[3, 5, 7], [3, 4, 5, ], [8, 5, 4]])
matrix2 = np.random.randint(1, 100, size=(3, 3))
print(matrix1+matrix2)
