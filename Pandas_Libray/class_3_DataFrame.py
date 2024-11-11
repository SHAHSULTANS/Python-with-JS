
# DataFrame actually multidimentioal table. Series is like a column, a DataFrame is like a whole table.

import pandas as pd
data={
    "calories":[400,650,450],
    "duration":[40,60,45]
}

df=pd.DataFrame(data)
print(df)


# Pandas use the loc attribute to return one or more specified row(s).

print(df.loc[[0,2]])