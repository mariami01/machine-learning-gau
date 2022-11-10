# დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს 3 რიცხვს და
# პროგრამა დაბეჭდავს რიცხვების საშუალო არითმეტიკულს.


def average_num(n1, n2, n3):
    return (n1+n2+n3)/3


num1 = float(input("Enter number #1: "))
num2 = float(input("Enter number #2: "))
num3 = float(input("Enter number #3: "))

avg = average_num(num1, num2, num3)
print('The average of numbers = ', avg)
