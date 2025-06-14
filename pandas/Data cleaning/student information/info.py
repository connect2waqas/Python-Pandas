# import pandas as pd

# df = pd.read_csv('studentinfo.csv')

# print(df["Name"].head(100)) # prints the first 100 names in the dataset?
# print(df["Age"].tail(100)) # prints the last 100 ages in the dataset

# print(df.describe())
# print(int(df["Age"].mean()))
# print(int(df["High School Percentage"].mean()))
# print(df.shape)
# print(df.memory_usage(deep=True))

# print(df.dtypes)

# print(df.columns)

# data = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=["Numbers"], index=['A','B','C','D','E','F','G','H','I','J'])
# print(data)

# print(df.head())
# print(df.sample(random_state=1)) it is used for random sampling of data
# print(df.sample(frac=0.5)) #it is used for sampling of 50% of the data

# print(df.loc[45:50, "Name":"Age" "Gender"]) # it is used to select the data between 45 to 50 index and name and age columns
# print(df.loc[45:50, ["Name", "Age", "Gender"]]) # it is used to select the data between 45 to 50 index and name and age columns

# print(df[df["Age"] == 23]) # it is used to select the data where age is 23
# print(df["Age"].mean()) # it is used to calculate the mean of the age column
# import pandas as pd

# df = pd.read_csv("C:\\Users\\dell\\OneDrive\\Desktop\\learning\\pandas\\pandas\\Data cleaning\\student information\\studentinfo.csv")

# print(df.loc[0:10, ["Name", "Age", "Gender","City"]]) # it is used to select the data between 0 to 10 index and name and age columns

# it is used to replace the age column with 10
# df.loc[4,"Gender"] ="Female"
# print(df)
# print(df.Name.str.capitalize()) # it is used to capitalize the first letter of the name column
# print(df["Age"].head(20).count()) # it is used to count the number of rows in the age column
# print(df.sort_values(["Age","High School Percentage"],ascending= False).head(20)) # it is used to sort the data in ascending order of the age column
# print(df.isnull().head(20))
# print(df.notnull().head(20)) # it is used to check the null values in the data
# df_filled = df.fillna({"Name": "Unknown", "Age": 0, "City": "ilyas"})
# print(df_filled.head(20))
# print(df.dropna())
# # print(df.duplicated().head(20)) # it is used to check the duplicate values in the data
# print(df.drop_duplicates())

import pandas as pd

df = pd.read_csv("C:\\Users\\dell\\OneDrive\\Desktop\\learning\\pandas\\pandas\\Data cleaning\\student information\\studentinfo.csv")

# print(df.dropna())
# print(df.duplicated().head(20)) # it is used to check the duplicate values in the data
# print(df.isnull())
# print(df.notnull()) # it is used to check the null values in the data
# df_replaced = df.fillna({"Name": "ilyas", "Age": 20, "City": "peshaware"})
# print(df_replaced)
# print(df["Age"]*2)
# print(df["Age"]+2)
# print(df["Age"]-2)
# print(df["Age"]/2)
# print(df["Age"]%2)
# # print(df["Age"]**2)
# print(df["Age"].mean())
# # print(df["Age"].median())
# df = pd.read_csv(r"C:\Users\dell\Downloads\data (1).csv")
# print(df.corr())
#Three lines to make our compiler able to draw:

# for index, row in df.iterrows():
#     print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}")
# for  row in df.itertuples():
    
#     print(f" index: {row.index}, Name: {row.Name}, Age: {row.Age}")

# for row , index in df.iterrows():
#     print(row)
#     print(index)
#     print("\n\n\n")