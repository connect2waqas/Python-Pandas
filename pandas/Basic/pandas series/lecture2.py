# What is a Series? 

# A pandas series is like column in a table

#  it has any type of data type

# import pandas as pd 

# a = [1,2,3,4]

# my_var = pd.Series(a)

# print(my_var[0]) # Accessing the index 

# the index can be name by you also .like

# my_var = pd.Series(a , index=['x','y','z','d'])

# print(my_var[0])
# print(my_var["x"])


import pandas as pd 

calorias = {"day1":"4","day2":"5", "day3":"8", "day4":"10"}

my_var = pd.Series(calorias,index = ["day1", "day2"])

print(my_var)