# წაიკითხეთ staff_1000.xls ფაილიდან მონაცემები გადაწერეთ 30-დან 40 წლამდე პერსონალის მონაცემები ახალ
# staff_age.xls ფაილში.
import pandas as pd
staff = pd.read_excel("staff_1000.xlsx", index_col=0)
staff_age = staff[(30 <= staff['Age']) | (staff['Age'] < 40)]
staff_age.to_excel("staff_age.xlsx")
