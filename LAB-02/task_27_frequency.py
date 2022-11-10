# იპოვეთ სიაში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5] ყველაზე ხშირად განმეორებადი რიცხვი.
#  დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ სიაში ყველაზე
#  ხშირად განმეორებადი რიცხვი.

arr = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]

count = 0
for i, item in enumerate(arr):
    for j, item1 in enumerate(arr):
        if (item == item1):
            count += 1

print(f"{item} occured {count} times in given array")
