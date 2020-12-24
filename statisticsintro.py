import pandas as pd
import numpy as np


health_data = pd.read_csv("health_data.csv", header=0, sep=",")

# Find percentile 
Max_Pulse = health_data[" Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
percentile25 = np.percentile(Max_Pulse, 25)
print(percentile10)
print(percentile25)