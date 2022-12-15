# წაიკითხეთ data.xlsx ექსელის ფაილის ყველა ფურცელი და გადაწერეთ მონაცემები datanew.xlsx ფაილში.
import pandas as pd
sheetOne = pd.read_excel('data.xlsx', sheet_name="sheetOne")
sheetOne = pd.read_excel('data.xlsx', sheet_name="sheetTwo")

new_data = pd.concat([sheetOne, sheetOne], axis=1)
new_data.to_excel("datanew.xlsx", index=False)
