# განსაზღვრეთ 6, 9 და 12 ელემენტიანი შემთხვევით [0, 100] შუალედიდან numpy
# მასივები და გააერთიანეთ.
import numpy as np

matrix1 = np.random.randint(1, 101, size=6)
print("matrix1")
print(matrix1)

matrix2 = np.random.randint(1, 101, size=9)
print("matrix2")
print(matrix2)

matrix3 = np.random.randint(1, 101, size=12)
print("matrix3")
print(matrix3)

print("merged matrix1, matrix2, matrix3 = ")
mergedMatrix = np.block([[matrix1, matrix2, matrix3]])
print(mergedMatrix)
