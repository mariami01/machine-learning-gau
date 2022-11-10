# დაწერეთ პროგრამა, რომელიც user-ს შეეკითხება თვეში სამუშაო საათების რაოდენობას და საათობრივ სახელფასო
# განაკვეთს. შედეგად დაბეჭდავს ყოველთვიური ხელფასის ოდენობას.
my_monthly_hour = float(input("how many hours do you work in a month?: "))
my_hour_salary = float(
    input("how much lari are you getting payed in an hour?: "))


def monthly_salary(monthly_hour, hour_salary):
    monthly_salary = monthly_hour * hour_salary
    return monthly_salary


print(monthly_salary(my_monthly_hour, my_hour_salary), "GEL")
