# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ორ ნებისმიერ რიცხვს.
# პროგრამამ შეამოწმოს, თუ ორივე შეყვანილი რიცხვი 10-ზე მეტია,
# დაითვალეთ მათი საშუალო არითმეტიკული, თუ არადა დაითვალეთ მათი
# ნამრავლი. დაბეჭდეთ მიღებული შედეგი.


num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if (num1 > 10) and (num2 > 10):
    print(num1+num2/3)
else:
    print(num1*num2)
