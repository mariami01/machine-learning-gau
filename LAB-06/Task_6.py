# წაიკითხეთ file_example_XLS_1000.xls ფაილიდან მონაცემები, დაბეჭდეთ მონაცემები ID-ის მიხედვით
# ზრდადობით, იპოვეთ Age-ის მიხედვით საშუალო არითმეტიკული, იპოვეთ საშუალო ასაკი, ასაკების მოდა,
# მედიანა, ყველაზე მაღალი და ყველაზე დაბალი ასაკის მომხარებელი.
import pandas as pd
df = pd.read_excel("file_example_XLSX_1000.xlsx", index_col=0)
df.sort_values(by=['Id'], ascending=True)
df["Age"].describe()

print(f"Age mean: {df['Age'].mean()}")
print(f"Age mode: {', '.join(str(m) for m in df['Age'].mode())}")
print(f"Age median: {df['Age'].median()}")
print("Oldest users: ")
print(df[df['Age'] == df['Age'].max()])
print("Youngest users: ")
print(df[df['Age'] == df['Age'].min()])
