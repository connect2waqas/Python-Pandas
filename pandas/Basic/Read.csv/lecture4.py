import pandas as pd

df = pd.read_csv("data.csv")

# print(df.head())  # First 5 rows
# print(df.tail())  # Last 5 rows
# print(df.info())  # Summary of the DataFrame
# print(df.describe())  # Statistical summary
# print(df.shape)  # (rows, columns)
# print(df.columns)  # List of column names
# print(df.info())  # Summary of the DataFrame    
# print(df[['Duration','Calories']]) # print(df[['Name', 'Age']])  # Selecting multiple columns
# print(df.dtypes)  # Data types of each column 
# print(pd.options.display.max_rows)  # Number of rows to display
pd.options.display.max_rows = 20 # Set the number of rows to display
print(df)