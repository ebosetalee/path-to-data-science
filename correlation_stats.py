import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


health_data = pd.read_csv("health_data.csv", header=0, sep=",")
health_data.plot(x =" Average_Pulse", y=" Calorie_Burnage", kind="scatter")
plt.show()

