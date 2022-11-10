# განსაზღვრეთ 36 ელემენტიანი შემთხვევით [0, 100] შუალედიდან მთელ რიცხვთა 1
# განზომილებიანი, 2 განზომილებიანი და 3 განზომილებიანი numpy მასივები და
# დაბეჭდეთ.

import numpy as np

#  1 D Matrix
matrix1 = np.random.randint(0, 100, size=36)
print("1D Matrix:")
print(matrix1)

#  2 D Matrix
matrix2 = np.random.randint(100, size=(6, 6))
print("2D Matrix:")
print(matrix2)


#  3 D Matrix
matrix3 = np.random.randint(0, 100, size=(2, 3, 6))
print("3D Matrix:")
print(matrix3)
