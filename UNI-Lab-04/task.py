import os
import numpy as np
import random
import datetime


def random_dates(start, end):
    dates = []
    for _ in range(100):
        dates.append(start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        ))
    return np.array(dates)


date1 = datetime.datetime.strptime("01-01-2019", '%d-%m-%Y')
date2 = datetime.datetime.strptime('31-01-2019', '%d-%m-%Y')

dataFile = open("data2.txt", "w")
for line in range(100, 999):
    dataFile.write("%s\n" % line)

dataFile.write(str(random_dates(date1, date2)))

dataFile.close()
