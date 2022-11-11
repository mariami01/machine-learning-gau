# მოცემულია ფორმულა y=3x-2, მოცემულია x-ის მნიშვნელობები, 
# რომლებიც წარმოადგენენ ათწილად რიცხვებს, რიცხვები დაშორებულია 
# ერთმანეთისგან „-“ ტირეებით 3,4–9-8.8-2 და ა.შ. შესაძლებელია მწკირვში 
# იყოს მაქსმიმუმ 10 რიცხვი, შესაბამისი სტრიქონი წინასწარ დააგენერირეთ შემთხვევითად, 
# დაწერეთ პროგრამა, რომელიც გამოითვლის შესაბამისი y-ის მნიშვნელობებს ზემოთ 
# მოცემული ფორმულის მიხედვით და შესაბამის x-ის და y-ის მნიშვნელობებს ჩაწერს ფაილში.

import random

def get_random_nums():
    nums_count = random.randint(1, 10)
    result = ''
    for _ in range(nums_count):
        random_float = round(random.uniform(0, 20), 2)
        result = f"{result}-{random_float}"
    return result.removeprefix('-')


def formula(x):
    return 3*x-2


nums = get_random_nums().split('-')
nums = [float(n) for n in nums]
with open("data_task1.txt", 'w') as f:
    text = ""
    for n in nums:
        text += f"y={formula(n)}, x={n}\n"
    f.write(text)