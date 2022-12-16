import numpy as np
import pandas as pd

import random
import datetime


def random_dates(start, end):
    dates = []
    for _ in range(100):
        dates.append(start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        ))
    return np.array(dates)


d1 = datetime.datetime.strptime("01-01-2019", '%d-%m-%Y')
d2 = datetime.datetime.strptime('31-01-2019', '%d-%m-%Y')
data = {
    "ID": np.random.randint(1000, 10000, size=100),
    "Date": random_dates(d1, d2),
    "Time": np.random.randint(1, 9, size=100),
    "Hourly_Wage": np.random.randint(10, 101, size=100)
}

df = pd.DataFrame(data=data)
df.loc[np.random.randint(0, 100, size=5), "ID"] = np.nan
df.loc[np.random.randint(0, 100, size=7), "Date"] = np.nan
df.loc[np.random.randint(0, 100, size=int(0.3*df.shape[0])), "Time"] = np.nan
df.loc[np.random.randint(0, 100, size=int(
    0.25*df.shape[0])), "Hourly_Wage"] = np.nan

df.to_excel('data.xlsx', sheet_name='sheetOne', index=False)
