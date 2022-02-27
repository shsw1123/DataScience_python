import pandas as pd
from IPython.display import display
# Read excel with read_csv()
df = pd.read_excel("Coffeshope.xlsx",sheet_name="Coffeshop")
# ถ้าเราต้องการทราบว่าสาขาไหนสามารถขายผลิตภัณฑ์ตัวไหนได้ดีที่สุด
#  Group by ด้วย สาขากับสินค้า
group_data = df.groupby(["branch","product"])
display(group_data.sum())
# ถ้าเราอยากรู้ว่าแต่ละสาขาขายเครื่องดื่มประเภทร้อนหรือเย็นได้ดีกว่ากัน
group_data_type = df.groupby(["branch","type"])
display(group_data_type.sum())
