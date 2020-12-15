import pandas as pd 


health_data = pd.read_csv("health_data.csv", header=0, sep=",")
print(health_data)

# use info() function to list data types:
print(health_data.info())
"""
where the dtypes shows object not int64 or float64,

use `astype()` function to convert the data:
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
print (health_data.info())

Because, we cannot use objects to calculate and perform analysis here.
"""

# Analyse data:
print(health_data.describe())