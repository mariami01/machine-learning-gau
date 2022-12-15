# შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით.
# დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.

nums = []
for _ in range(10):
    nums.append(int(input("Number: ")))


avg = sum(nums)/10
print(avg)
