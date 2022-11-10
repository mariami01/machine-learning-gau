# შეიტანეთ ათწილადი რიცხვი, დაამრგვალეთ ათწილად ნაწილში მეათედის
# სიზუსტით (1 ციფრი ათწილად ნაწილში) და დაბეჭდეთ შედეგი. გამოიყენეთ
# round, ceil, floor, trunc ფუნქციები სათითაოდ და შეამოწმეთ შედეგი თითოეულის
# გამოყენებით.
import math

num = float(input("Enter a number: "))

print(round(num, 1))
print(math.ceil(num))
print(math.floor(num))
print(math.trunc(num))
