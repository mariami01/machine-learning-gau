# შექმენით ლექსიკონი: {0: 10, 1: 20}. დაამატეთ 2 ახალი ელემენტი და დაბეჭდეთ
# მიღებული ლექსიკონი. (გამოიყენეთ update მეთოდიც). წაშალეთ რომელიმე
# ელემენტი.


dict = {0: 10, 1: 20}

dict[2] = 30
dict[5] = 40
dict[6] = 50
dict[7] = 60
print(dict)

dict.update({2: 25})
print(dict)

dict.pop(1)
print(dict)

dict.popitem()
print(dict)

del dict[0]
print(dict)
