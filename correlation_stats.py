import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


health_data = pd.read_csv("health_data.csv", header=0, sep=",")
health_data.plot(x=" Average_Pulse", y=" Calorie_Burnage", kind="scatter")
# plt.show()
print(health_data.corr())


corr_matrix = round(health_data.corr(), 2)
print(corr_matrix)


axis_cor = sn.heatmap(corr_matrix, vmin=-1, vmax=1, center=0,
                      cmap=sn.diverging_palette(50, 500, n=500), square=True)
plt.show()
# scipy is for scientific calculations
# figure_11.png