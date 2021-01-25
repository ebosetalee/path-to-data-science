import pandas as pd
import matplotlib.pyplot as plt


drowning_accident = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
ice_cream_sale = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

drowning = {"Drowning_Accident": drowning_accident, "Ice_Cream_Sale": ice_cream_sale}

drowning = pd.DataFrame(drowning)
drowning.plot(x="Drowning_Accident")
plt.ylabel("Ice_Cream_Sale")
plt.title("Beach")
plt.show() # figure_12.png

corr_d = drowning.corr()
print(corr_d)