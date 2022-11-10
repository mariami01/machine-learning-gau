# დაწერეთ პროგრამა, რომლის გაშვებისას შეიყვანთ ნებისმიერ რიცხვს.
# იპოვეთ შეყვანილი რიცხვის ბოლო ციფრი და დაბეჭდეთ ეკრანზე.

my_num = int(input("Enter a number: "))

last_digit = my_num % 10

print(f"The Last Digit of {my_num} is {last_digit}")
