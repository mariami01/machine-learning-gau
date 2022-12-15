# წაიკითხეთ data.xlsx ექსელის ფაილის „sheetOne“ ფურცლიდან მონაცემები იპოვეთ პირველ სვეტში ჩაწერილი
# სტრიქონებიდან რომელი შეიცავს სიმბოლო ‘a’-ის და გადაწერეთ datanew.xlsx ფაილის “sheet3” ფურცელში.
import pandas as pd
sheetOne = pd.read_excel('data.xlsx', sheet_name="sheetOne")

# substring to be searched
sub = 'a'

# creating and passing series to new column
data["Indexes"] = data["rand_name"].str.find(sub)

# display
# data

with pd.ExcelWriter("datanew.xlsx", engine="openpyxl", mode="a") as writer:
    data.to_excel(writer, sheet_name="sheet3", index=False)
