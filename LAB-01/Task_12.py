# დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.


num = 0

for num in reversed(range(25, 201)):
    if num == 1:
        print(num)
    if num % 8 == 0:
        print(num)
