import random

#Generate a random interger two number
rNumber=random.randint(5,10)
print(rNumber)



#Generate a random number betwween 0 and one (Floating)
print(random.random())



#Generate a random number betwween 5 and 10 (Floating)
print(random.uniform(5,10))





#Select a random sequence from list
#one is choice return a single 
#another is choices return a list
fruits=["Apple","Banana","Cherry","Jackfruit","Orange"]
randomChoices=random.choice(fruits)
print(randomChoices)



#Choices Two random Elements from list
sampleTwo=random.sample(fruits,2)
print(sampleTwo)



#suffle a list
random.shuffle(fruits)
print(fruits)



#numpy libray
    #Used image processing (MRI, CT scan)
    #IoT(temperature, humidity, motion sensor) collect data then analysize.
    #Machine learning(Developing a predictive model for customer behavior or predict customer churn)
