import matplotlib.pyplot as plt
import pandas as pd 


health_data = pd.read_csv("health_data.csv", header=0, sep=",")
health_data.plot(x=" Average_Pulse", y=" Calorie_Burnage", kind="line")

plt.ylim(ymin=0)
plt.xlim(xmin=0)
# you can add the max e.g ymax = 400 or xmax = 150

# plt.show() files/Figure_1.png

