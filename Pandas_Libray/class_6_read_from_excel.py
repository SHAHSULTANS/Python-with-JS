

import pandas as pd


df=pd.read_excel("F:\linuxPractice\pandas_practice.xlsx",usecols="B")

print(df )

print("\nConvert rettrieve data as a list")
column_as_list = df["email"].tolist()
print(column_as_list)