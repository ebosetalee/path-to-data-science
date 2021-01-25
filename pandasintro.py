import pandas as pd
import numpy as np 


data = {"column1": [1, 2, 3, 4, 5],
        "column2": [4, 5, 6, 9, 5],
        "column3": [7, 8, 12, 1, 11]}

factored = pd.DataFrame(data=data)
print(factored)

# count the number of columns
count_column = factored.shape[1]
print("column = ", count_column)

# count the number of rows
count_row = factored.shape[0]
print("Rows = ", count_row)

# We have min(), max(), mean()
data_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("Minimum is ", data_min)

data_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print("Maximum is", data_max)

# For mean, we need to import numpy
# for numpy.mean, it takes 5 arguments. Thus, place the values in a variable.
values = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
data_mean = np.mean(values)
print("Mean is ", data_mean)
