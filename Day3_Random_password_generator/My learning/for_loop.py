

#Basic for Loop.
fruits=["apple","banana","chery","orange"]
fruits.append("Grapes")
fruits.pop()
print(len(fruits))

for x in fruits:
    print(x,end=" ")
print()  
    
  
    
#Basic for loop with range
for i in range(-1,5,1):
    print(i, end=" ")
print()    



#Looping through the dicionary.Remove duplicate, conside the latest.
person={"name":"Shanto","age":"23","age":40}
#In JavaScript you can access it using dot noation.You can also access like python.
print(person["name"])
for key in person.items():
    print(key)
    

#enumerate use for getting index along with value.
for index,fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    
    

#zip() allows you to loop over multiple sequences in parallel, combining items at the same index.iterate up to shortest list.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")



#reading data from a file/ or append text to the file
with open("Day3\My learning/general.txt","r") as file:
   # print(file.write("This text append to the file"))
   print(file.read())