# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. შეცვალეთ ყველა
# 0-ის მნიშვნელობა 1-ით. გამოიყენეთ numpy ბიბლიოთეკა.


import numpy as np

matrix = np.random.randint(0, 10, size=(10, 10))
# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. შეცვალეთ ყველა
# 0-ის მნიშვნელობა 1-ით. გამოიყენეთ numpy ბიბლიოთეკა.


matrix = np.random.randint(0, 10, size=(10, 10))
print(matrix)

# indices_one = matrix == 1
indices_zero = matrix == 0

# matrix[indices_one] = 0 # replacing 1s with 0s
matrix[indices_zero] = 1  # replacing 0s with 1s
print("______________")

print(matrix)
