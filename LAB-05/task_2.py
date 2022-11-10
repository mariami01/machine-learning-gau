# განსაზღვრეთ 36 ელემენტიანი შემთხვევით [0, 100] შუალედიდან მთელ რიცხვთა 1
# განზომილებიანი მასივი, გადაიყვანეთ ყველა შესაძლო 2 განზომილებიან, 3
# განზომილებიან მასივად და დაბეჭდეთ.

import numpy as np

#  1 D Matrix
matrix1 = np.random.randint(0, 100, size=36)
print("1D Matrix:")
print(matrix1)

# 2 D Matrix

matrix2 = matrix1.reshape(6, 6)
print("2D Matrix:")
print(matrix2)

# 3 D Matrix
matrix3 = matrix1.reshape(2, 3, 6)
print("3D Matrix:")
print(matrix3)
