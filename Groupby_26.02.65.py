import pandas as pd
import numpy as np

# groupby() have 3 method **page 193
# split คือ การเอาข้อมูบมาแตกออกเป็นกลุ่มๆ โดยจัดข้อมูลที่ซ้ำๆ กันไว้ในกลุ่มเดียวกัน
# Apply คือ การนำเอาข้อมูลในแต่ละกลุ่มมาดำเนินการด้วยฟังก์ชั่นต่างๆ เช่น การหาผลรวม ค่าเฉลี่ย หาค่าสูงสุด ต่ำสุด
# Combine คือ การเอาข้อมูลของแต่ละกลุ่มมารวมกัน

# Create list
list_data = [11, 21, 31, 32, 22, 12, np.NaN]
# Create index of list
index_list = ["A","B","C","C","B","A","D"]
# Create Series
series = pd.Series(data=list_data,index=index_list)
print("นับจำนวนข้อมูลด้วย Count จะไม่นับ NaN")
print(series.groupby(index_list).count())
print("นับขนาดของกลุ่มด้วย size จะนับรวม NaN ด้วย")
print(series.groupby(index_list).size())
print("หาค่าต่ำสุด-สูงสุดของข้อมูลในแต่ละกลุ่ม")
print(series.groupby(index_list).agg([min,max])) # agg is ตัวดำเนินการ



