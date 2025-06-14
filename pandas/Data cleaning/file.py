import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')

# new_df = df.dropna()

# print(new_df.to_string())

# df.fillna("waqas", inplace=True)

# print(df.to_string())

# df["Calories"].fillna(500, inplace=True)

# print(df.to_string()

# df = pd.read_csv('data.csv')

# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)

# print(df.to_string())

# print(df.replace(" ", np.nan))

# newdf = df['Calories'] = df['Calories'].apply(str.lower)

# print(newdf)
# newdf = df.drop_duplicates().count()
# print(newdf.to_string())

df = pd.read_csv('data.csv')

# for index , row in df.iterrows():
#     # print(index)
#     print(row[["Pulse","Maxpulse"]])

data_info = (int(df["Duration"].mean()*2))
data_info1 = (int(df["Pulse"].median()*2))

sum = data_info + data_info1
print(float(sum) + 23.33) 

average = (data_info + data_info1) // 2
num = input("enter a number ")
if num > average:
    print("enter a ")

