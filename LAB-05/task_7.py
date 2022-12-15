# განსაზღვრეთ ორი 12 ელემენტიანი შემთხვევით [0, 100] შუალედიდან numpy
# მასივები, იპოვეთ შიდა, გარე და ჯვარედინი ნამრავლი.
import numpy as np

matrix1 = np.random.randint(1, 101, size=(2, 6))
print("matrix1")
print(matrix1)

matrix2 = np.random.randint(1, 101, size=(2, 6))
print("matrix2")
print(matrix2)


print("\nInner product of matrices matrix1 and matrix2 =")
print(np.inner(matrix1, matrix2))

print("\nOuter product of matrices matrix1 and matrix2 =")
print(np.outer(matrix1, matrix2))

print("\nCross product of matrix1 and matrix2 =")
print(np.cross(matrix1, matrix2, axis=0))
