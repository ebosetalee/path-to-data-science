"""
Developed by John D Hunter and derived from MatLab
It is a MatLab for python and depends on numpy. It is for graphical represntations.

Using pyplot module.
plot is a function that belongs to the pyplot module.
"""


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


# default line is blue but can be chnaged.
# More functions include:
"""title()
xlabel()
figure()""" # specify the size

"""
plt.figure(figsize=(15, 5))
plt.plot([1, 2, 3, 4], [10, 20, 30, 40], "go")
plt.title("Sales Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
# plt.show()""" #figure_7.png
# The go siginifies g- green, o - circles.
# you can graph more than one data:
"""x = np.arange(1,5)
y = x**5
plt.plot([1, 2, 3, 4], [10, 20, 30, 40], "go", x, y, "r^")
# plt.show()""" #figure_6.png

# Different calculations can be done using np
"""
x_line = np.arange(0, 6, 0.2)
y_line = np.sin(x_line)
plt.plot(x_line, y_line)
plt.show() """ #figure_8.png

# Bar Graph:
"using plt.bar()"
month = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [50, 65, 55, 70, 50]
"""
plt.bar(month, sales, width=0.5, color="green")
"""
plt.barh(month, sales, height=0.5, color="green")
plt.title("Sales Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show() #figure_9.png
# for horizontal use plt.barh()  - figure_10.png