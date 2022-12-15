# შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ. თუ
# კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.
import math
nums = []
for _ in range(10):
    nums.append(int(input("Number: ")))

odd_nums = []
for i in nums:
    if i % 2 != 0:
        odd_nums.append(i)

max_odd = max(filter(lambda x: x % 2 == 0, odd_nums))

print(max_odd)
# else:
#     print("No Odd Number Given Here ;(")
