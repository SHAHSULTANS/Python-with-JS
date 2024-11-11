
# A pandas series is like a column in a table.

# One dimensional array holding data of any type.

import pandas as pd



#create a series from a list.
a=[6,9,2,0]
myvar=pd.Series(a)
print(myvar)


#create own label
print("\nCreate own label/index")
myvar2=pd.Series(a,index=["a","b","c","d"])
print(myvar2)



#using dictionary in series. The key is used as a label/index.
print("\n Using dictionary in series")
calories={"day1":400,"day2":450,"day3":430}
myvar3=pd.Series(calories)
print(myvar3)