
# Big Data set are stored or extracted as JSON.

import pandas as pd

data=pd.read_json('Pandas_Libray/data.json')

print(data.to_string())#to_string() print entire.