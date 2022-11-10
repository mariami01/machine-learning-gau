# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ წელს და დაადგენთ არის თუ არა შეყვანილი რიცხვი ნაკიანი წელიწადი.

my_year = int(input("Enter a year: "))


def find_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"Leap Year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


find_leap_year(my_year)
