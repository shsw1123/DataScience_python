import pandas as pd
import numpy as np
my_df = np.array([["Player1", "ABC", 256],
                  ['Player2', "Sky", 320],
                  ["Player3", "ABC", 185],
                  ["Player4", "Sky", 225],
                  ["Player5", "Rotation", 333],
                  ["Player6", "MomoMama", 210]])

df = pd.DataFrame(my_df,columns=["Player name","Team name","Score"],index=["A","B","C","D","E","F"])

for Key, Value in df.iteritems():
    print(Key)  # Key = index
    print(Value)

print("--------------------------------")

for Key, Value in df.iterrows():
    print(Key,Value)

print("--------------------------------")

for i in df.itertuples():
    print(i)