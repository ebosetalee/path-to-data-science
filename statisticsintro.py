import pandas as pd
import numpy as np


health_data = pd.read_csv("health_data.csv", header=0, sep=",")

# Find percentile 
Max_Pulse = health_data[" Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
percentile25 = np.percentile(Max_Pulse, 25)
print(percentile10)
print(percentile25)
print("--" * 40)


# Find Standard Deviation
standard_deviation = np.std(health_data)
print(standard_deviation)
print("--" * 40)

# Coefficient of Variation
c_of_v = np.std(health_data) / np.mean(health_data)
print(c_of_v)
print("--" * 40)

# Calculate variance
def calc_variance(data):
    result = 0
    for item in data:
        result += item
    mean = result/ len(data)
    final_variance = 0
    for items in data:
        mean_difference = items - mean
        square_value =  mean_difference ** 2
        final_variance += square_value
    return final_variance / len(data)
print(calc_variance(health_data[" Average_Pulse"]))

# A simple method is to use numpy built-in function var()
variance = np.var(health_data[" Average_Pulse"])
print(variance)
full_variance = np.var(health_data)
print(full_variance)