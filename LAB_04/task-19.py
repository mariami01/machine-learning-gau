# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ
# კლავიატურიდან შეტანილი რიცხვი. გამოიყენეთ numpy ბიბლიოთეკა.

import numpy as np

matrix = np.random.randint(0, 10, size=(10, 10))
num = int(input("Enter a num: "))
matrix = np.delete(matrix, num)
print(matrix)
