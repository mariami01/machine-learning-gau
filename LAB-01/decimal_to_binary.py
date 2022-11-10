# დაწერეთ პროგრამა, რომელიც შეყვანილ ათობით რიცხვს გადაიყვანს ორობითში.
def decimalToBinary(n):
    if n > 1:
        decimalToBinary(n//2)
    print(n % 2, end='')


num = int(input("Enter a number: "))
decimalToBinary(num)
print()
