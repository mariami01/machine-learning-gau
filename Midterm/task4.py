# შეავსეთ ორი 10x10 მატრიცა შემთხვევითი მთელი რიცხვებით [a, b] შუალედიდან. 
# გადაიყვანეთ ორივე მატრიცა ერთ ლისტად. გამოიყენეთ numpy ბიბლიოთეკა.
#0 იპოვეთ პირველი მატრიცის მოდა, ხოლო მეორე მატრიციდან მაქსიმალურსა და მინიმალურ შორის სხვაობა. 
import numpy as np
import numpy
from scipy import stats

range_from = int(input("Range from: "))
range_to = int(input("Range to: "))
print("--------------------------------")

# generate matrix1
matrix1 = np.random.randint(range_from, range_to, size=5)
print("#1 Matrix:")
print(matrix1)
print("--------------------------------")

# generate matrix2
matrix2 = np.random.randint(range_from, range_to, size=5)
print("#2 Matrix:")
print(matrix2)
print("--------------------------------")
#  Concat matrices 
matrix=np.concatenate((matrix1,matrix2))
print("Concatenating Matrix1 and Matrix2: ")
print(matrix)
print("--------------------------------")

# Matrix1 Mode
count = 0
for i, item in enumerate(matrix1):
    for j, item1 in enumerate(matrix1):
        if (item == item1):
            count += 1
print(f"Mode of the Matrix1 is {item},it occured {count} times.")
print("--------------------------------")

# Max-Min [Matrix2]
print(f"Matrix2 maximum number = {numpy.max(matrix2)},min = { numpy.min(matrix2)}")
print(f"Max - Min = {numpy.max(matrix2)- numpy.min(matrix2)}")





