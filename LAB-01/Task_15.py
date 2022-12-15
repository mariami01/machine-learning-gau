# დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.

def even_num_sum(num1, num2):
    even_num = []
    for num in range(num1, num2):
        if num % 2 == 0:
            even_num.append(num)

    num_sum = sum(even_num)
    return num_sum


even_num_sum(1, 100)
