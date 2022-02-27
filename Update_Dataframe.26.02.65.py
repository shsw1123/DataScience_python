import pandas as pd
import numpy as np
# Create array
data = np.array([["Snack1",10],
                 ["Snack2",20],
                 ["Snack3",30]])
# Create Dataframe
df = pd.DataFrame(data=data,columns=["Product","price"])

# Update data column price
for i in df.index:
    df.at[i,"price"] = pd.to_numeric(df.at[i,"price"])+5

print(df)

# Update Data row price
df.at["0","price"] = 17 # "0" is location of row
print("Update price of snack1 additional 2 bath so new price is",df.loc["0","price"])

