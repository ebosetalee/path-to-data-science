import numpy as np
import pandas as pd


def slope(x1, y1, x2, y2):
    solution = (y2-y1)/(x2-x1)
    return int(solution)

print (slope(80,240,90,260))

health_data = pd.read_csv("health_data.csv", header=0, sep=",")

x = health_data[" Average_Pulse"]
y = health_data[" Calorie_Burnage"]

slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)

def calculate(x):
    solution = (2 * x) + 80
    return int(solution)

print(calculate(135))
print(calculate(125))
