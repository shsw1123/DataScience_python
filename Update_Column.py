import pandas as pd
import numpy as np
# Create array from numpy comand
my_df = np.array([["Player8", "NumberOne", 256],
                  ["Player7", "NumberTwo", 256],
                  ["Player1", "NumberOne", 256],
                  ["Player9", "NineNine", 225],
                  ["Player5", "FiveStar", 333],
                  ["Player6", "SixZipZa", 210]])
# Create Dataframe from array
df = pd.DataFrame(data=my_df,columns=["Player Name","Team Name","Score"],index=["8","7","1","9","5","6"])
df_1 = df
# Rename Column
df_new = df.rename(columns={"Team Name" : "Club Name"})  # Good
print(df_new)
print(df.rename(columns={"Team Name" : "Club Name"}))  # Also Good
print("#############################")
# Add New column with create list
age = ["18","23","20","18","19","19"]
df_new["Age"] = age
print(df_new)
print("#############################")
# Add New column with insert function
# Dataframe.insert(location, Name column, Data, allow_duplicates)
df.insert(1,"Age",age,allow_duplicates=False)
print(df)
print("#############################")
# Add New column with assign function
# Dataframe = dataframe.assign("Name column")
df_1 = df_1.assign(อายุ = [18,23,20,18,19,19])
print(df_1)
print("###################################################################")



