# import pandas as pd

# df = pd.read_csv(r"c:\Users\ztech.pk\Downloads\stack-overflow-developer-survey-2019\survey_results_public.csv")
# # print(df.info())
# # print(df.shape)
# # print(df.columns)
# # print(df.describe())
# # pd.set_option("display.max_columns",85)
# schema_df = pd.read_csv(r"c:\Users\ztech.pk\Downloads\stack-overflow-developer-survey-2019\survey_results_schema.csv")
# # print(df["QuestionText"].head(10))

# print(schema_df)

import pandas as pd
import numpy as np

dates = pd.date_range("2023-01-01", "2023-03-31",freq="D")

stores = ["North","South","East","West"]

products = ["Electronics","Clothing","Groceries"]

index = pd.MultiIndex.from_product([stores,products,dates],names=["Store", "Product", "Date"]
)

np.random.seed(42)
sales = np.random.randint(100, 1000, size=len(index))
df = pd.DataFrame({"Sales": sales}, index=index)

df = df.reset_index()
print(df)
print(df.index)
print(df.info()