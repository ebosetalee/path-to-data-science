"""
What is Numpy?
Numpy is an open source library in python that used 
mathematical, statistical operations, scientificc, 
engineering and data science programming.

Operations using numpy:
- calculations etc
- array function `np.array()` # Notice the difference: without commas
- shape - states the rows and columns of the list seperated by comma.
- shape()
- dtype - to check the internal data type in numpy library
- ndmin - dimension array - single, 2, multiple dimension #note the brackets;
            it has one row and 5 columns.
- 
"""
import numpy as np


list_a = [10, 20, 30, 40, 50]
print(list_a)
print(type(list_a))

print("--" * 40)

list_b = np.array(list_a)
print(list_b)
print(type(list_b))

print("--" * 40)
print(list_b + 100)

print("--" * 40)
print(list_b.shape)

print("--" * 40)
print(list_b.dtype)

print("--" * 40)
list_c = np.array([10.3, 20.7, 30.4, 40.5, 50.0])
print(list_c.dtype) 

print("--" * 40)
list_d = np.array(list_a, ndmin=2)
print(list_d)
print(list_d.shape)

print(list_c.shape)

list_e = np.array([[1, 2, 3], [4, 5, 6]])
print(list_e.shape)
#list_e.shape = (3,2) # This changes the shape
#print(list_e)

# You can switch a numpy array to dataframe
import pandas as pd
print(list_e)
df = pd.DataFrame(list_e)
print(df)

# you can also switch pandas dataframe to numpy array:
df_array = np.array(df)
print(df_array)