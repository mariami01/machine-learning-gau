# მთელი 24, 39, -90 რიცხვები ჩაწერეთ data.txt ფაილში, ფაილი შექმენით myFiles
# საქაღალდეში.
import os

if not os.path.exists("myFiles"):
    os.mkdir("myFiles")

with open("myFiles/data.txt", "w") as f:
    f.write("24, 39, -90")
