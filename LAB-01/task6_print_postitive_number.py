# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს.
# თუ რიცხვი დადებითია, დაბეჭდოს ეკრანზე “Number is positive”.

num = float(input("Enter a number: "))


def check_positive_number(number):
    if num >= 0:
        return "Number is Positive!"


print(check_positive_number(num))
