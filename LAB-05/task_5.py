# განსაზღვრეთ 5x3 და 3x2-ზე მასივები, რომლებიც შეავსეთ შემთხვევითი მთელი
# რიცხვებით [0, 100] შუალედიდან, იპოვეთ პირველის მეორეზე ნამრავლი.
import numpy as np

matrix1 = np.random.randint(1, 101, size=(5, 3))
print("matrix1")
print(matrix1)

matrix2 = np.random.randint(1, 101, size=(3, 2))
print("matrix2")
print(matrix2)

print("matrix1 * matrix2=")
print(matrix1.dot(matrix2))
