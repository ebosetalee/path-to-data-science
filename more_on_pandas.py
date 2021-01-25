import pandas as pd


val = [10, 20, 30]
print(pd.Series(val))
print(pd.Series(val, index = ["a", "b", "c"]))

ser = pd.Series(val)
print(type(ser))

school_list = [["Samuel", 95], ["James", 52], ["Cynthia", 85], ["Sharon", 90]]
print(school_list)
df = pd.DataFrame(school_list)
print(df)

# You can change columns by:
df_columns = pd.DataFrame(school_list, columns=["Name", "Score"])
print(df_columns)

# To print a particular column:
print(df_columns["Name"]) #checking by column is series 

what_type = df_columns["Name"]
print(type(what_type)) # series
# If you combine two series, it is a dataframe. 
value = {"Name": ["Samuel", "Jane"], "Age": [40, 35]}
value_df = pd.DataFrame(value)
print(value_df)
