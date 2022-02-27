import pandas as pd
import numpy as np
from IPython.display import display
# Create Data and column
data = { "EmpName" : ["Emp1","Emp2","Emp3","Emp4","Emp5",
                      "Emp6","Emp7"],
         "Dept" : ["Team1","Team1","Team1","Team1","Team2",
                   "Team2","Team2"],
         "Salary" : [25600, 32500, 18000, 20000, 85000,
                     85000, 70000] }
# Create dataframe
df = pd.DataFrame(data=data)
# Split df by Dept column
g_data = df.groupby("Dept")
# Display
display(g_data.get_group("Team1"))
display(g_data.get_group("Team2"))

# Split, Apply, Combined
display(df.groupby("Dept")["Salary"].agg([min,max,sum]))