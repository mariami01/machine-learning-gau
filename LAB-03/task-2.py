# 0-დან 100-მდე მთელი რიცხვები ჩაწერეთ data1.txt ფაილში. myFiles
# საქაღალდეში.
import os

if not os.path.exists("myFiles"):
    os.mkdir("myFiles")

dataFile = open("myFiles/data1.txt", "w")
for line in range(100):
    dataFile.write("%s\n" % line)
dataFile.close()
