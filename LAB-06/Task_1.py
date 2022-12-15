#  ჩაწერეთ data.xlsx ექსელის ფაილის „sheetOne“ ფურცელზე 100 მონაცემი (100 სტრიქონი).
#  პირველ სვეტში ჩაწერეთ ათი სიმბოლოსგან შემდგარი შემთხვევითი სტრიქონი;
#  მეორე სვეტში ჩაწერეთ შემთხვევითი რიცხვები [0, 10] შუალედიდან;
#  მესამე სვეტში ჩაწერეთ შემთხვევითი რიცხვები [1, 7] შუალედიდან;
#  მეოთხე სვეტში ჩაწერეთ შემთხვევითი განსხვავებული რიცხვები [1, 100] შუალედიდან.

import numpy as np
import pandas as pd

import string

ALPHABET = np.array(list(string.ascii_lowercase + string.ascii_uppercase))

dt = {
    'rand_string': [''.join(np.random.choice(ALPHABET, size=10)) for _ in range(100)],
    'rand_1_10': np.random.randint(0, 11, size=100),
    'rand_1_7': np.random.randint(1, 8, size=100),
    'rand_unique': np.random.choice(100, size=100, replace=False)
}

data = pd.DataFrame(data=dt)
data.to_excel('datasets/data.xlsx', sheet_name="sheetOne", index=False)
