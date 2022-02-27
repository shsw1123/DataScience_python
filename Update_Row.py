import pandas as pd
import numpy as np
# How to add row in Dataframe
# Dataframe.append(Dataframe, ignore_index,  verify_integrity)  *page 188

Data1 = np.array([["Player8", "NumberOne", 256],
                  ["Player7", "NumberTwo", 256],
                  ["Player1", "NumberOne", 256],
                  ["Player9", "NineNine", 225],
                  ["Player5", "FiveStar", 333],
                  ["Player6", "SixZipZa", 210]])
# Create new array
Data2 = np.array([["New_Player88",280],
                   ["New_Player77",320]])
# Create Dataframe from array
Dataframe1 = pd.DataFrame(data=Data1,columns=["Player Name","Team Name","Score"],index=["8","7","1","9","5","6"])
# create New Dataframe
Dataframe2 = pd.DataFrame(data=Data2,columns=["Player Name","Score"])
# Insert row
print(Dataframe1.append(Dataframe2))
print(Dataframe1.append(Dataframe2,ignore_index=True))


# Delete column & Row in dataframe
# Delete column used drop("Name column",axis=1)
drop_column_by_labe1 = Dataframe1.drop("Team Name",axis=1)
# Delete row used drop(["index","index"])
drop_row_by_labe1 = Dataframe1.drop(["8","7"])
print(drop_row_by_labe1)
print(drop_column_by_labe1)