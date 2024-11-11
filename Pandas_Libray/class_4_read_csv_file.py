
# CSV--> (comma separated value) where data organized in a tabular format.


import pandas as pd

tablularcsv=pd.read_csv("Pandas_Libray/data.csv.txt")
print(tablularcsv.to_string())# Here to string is used print entire data if takes 100vh then add overflow-y:auto.


print("\nChecked maximu rows return in Pandas option setting")
print(pd.options.display.max_rows)