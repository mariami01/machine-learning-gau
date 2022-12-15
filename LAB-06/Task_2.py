# დაამატეთ data.xlsx ექსელის ფაილის „sheetTwo“ ფურცელზე 50 მონაცემი (50 სტრიქონი).
# პირველ სვეტში ჩაწერეთ განსხვავებული რიცხვები [1, 100] შუალედიდან.
# მეორე სვეტში ჩაწერეთ შემთხვევით სახელები (სახელი შეარჩიეთ წინასწარ გასზაღვრული მასივიდან);
# მესამე სვეტში ჩაწერეთ შემთხვევით გვარები (გვარი შეარჩიეთ წინასწარ გასზაღვრული მასივიდან);
# მეოთხე სვეტში ჩაწერეთ შემთხვევითი რიცხვები [2000, 5000] შუალედიდან.

import numpy as np
import pandas as pd

rand_names = ['nino', 'gela', 'vazha', 'gio', 'lela', 'tamari']
rand_lastnames = ['lezhava', 'bakuria',
                  'chkhenkeli', 'chkhaidze', 'bakradze', 'nozadze']
dt = {
    'rand_nums': np.random.randint(1, 101, size=50),
    'rand_name': np.random.choice(rand_names, size=50),
    'rand_lastname': np.random.choice(rand_lastnames, size=50),
    'rand_nums': np.random.randint(2000, 5001, size=50)
}

data = pd.DataFrame(data=dt)
with pd.ExcelWriter("data.xlsx", engine="openpyxl", mode="a") as writer:
    data.to_excel(writer, sheet_name="sheetTwo", index=False)
