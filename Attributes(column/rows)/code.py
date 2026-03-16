import pandas as pd
def intro():
  data = pd.read_csv("sales_data_sample.csv", encoding="latin1")
  print("Displaying the shape of the data:")
  rows , columns = data.shape
  print(f"row: {rows},\ncolumns: {columns}")
  columns_names = data.columns # display the column labels
  print(columns_names)
  row_names = data.index
  print("\n", row_names)
intro()
