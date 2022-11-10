# myFiles1 საქაღალდეში საქაღალდეში შექმენით 30 ფაილი, ფაილებში ჩაწერეთ
# სიტყვა „Programmer“.

import os

if not os.path.exists("myFiles1"):
    os.mkdir("myFiles1")

number_of_files = 5
for i in range(number_of_files):
    file_name = f"file_{i+1}.txt"
    with open(f"myFiles1/{file_name}", "w") as f:
        f.write("Programmer")
