#printing console primarly accomplished with the print function.



# #in Python backtrick characters are not used.


print("Hello Shanto\nWeclome to Our python Journey")
print("Hello Shanto\tWeclome to Our python Journey")


name=input("Enter your Name: ")
age=20
print("Name:",name, "Age:",age)

print(f"Name {name}")


print("I am {}".format(name))
#end specifies what to print at the end of the line(default is a newline)

print("Name","age", sep=",", end="!!")



number=input("Enter a number: ")

#This is called variabale Casting.
number=int(number)
print(type(number))

if(number==5):
    print("True")
else:
    print("False")





