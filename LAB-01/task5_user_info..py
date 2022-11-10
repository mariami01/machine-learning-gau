# დაწერეთ პროგრამა რომელიც შეეკითხება user-ს სახელს და ასაკს.
# გამოთვალეთ რამდენ წელში გახდება 100 წლის და დაბეჭდეთ შესაბამისი ინფორმაცია.

name = input("What's your name?: ")
age = int(input("How old are you?: "))


def years_till_100(user_name):
    return 100-user_name


print(f"{name} will turn 100 in {years_till_100(age)} years :)")
