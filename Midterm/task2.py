# დაწერეთ პროგრამა, რომელიც შეტანილ სტრიქონის მიხედვით, რომელიც აუცილებლად შეიცავს ინგლისური ანბანის დიდ ან პატარა ასოებს და ციფრებს, 
# დაბეჭდავს ცალკე ინგლისური ანბანის ასოებისგან შემდგარ სტრიქონს, ცალკე ციფრებისგან შემდგარ სტრიქონს და  შესაბამისად თითოეულ მათგანს გვერდზე მიუწერს სიმბოლოების რაოდენობას. 
# მაგალითად: შეტანილი სტრიქონი hello 87 my 65  world; გამოვავალი სტრიქონები: hellomyworld – 12; 8765 - 4


import string


alpabet = string.ascii_letters
nums = '1234567890'

text = input("Enter string: ").replace(" ", "")

characters = ""
characters_count = 0
numbers = ""
numbers_count = 0
for char in text:
    if char in alpabet:
        characters += char
        characters_count += 1
    else:
        numbers += char
        numbers_count += 1

print(f"{characters} - {characters_count}")
print(f"{numbers} - {numbers_count}")