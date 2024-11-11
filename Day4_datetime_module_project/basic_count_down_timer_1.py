
import datetime
import os
import time
 
# gettime=input("Enter Your ending time(YY-MM-DD-HH-MM-SS")
# print(gettime)
currentYear=datetime.datetime.now().year
# print(currentYear)
endtime=datetime.datetime(currentYear+1,5,27,23,59,59)

while True:
    now=datetime.datetime.now()
    timeRemaining=endtime-now
    # print(timeRemaining)(
    # print(timeRemaining.total_seconds())
    
    days=timeRemaining.days
    if(timeRemaining.total_seconds()<=0):
        break
    
    hours=timeRemaining.seconds//3600
    minites=(timeRemaining.seconds%3600)//60
    seconds=timeRemaining.seconds%60
    print(f"Time is Remaining: {days} days, {hours} hours, {minites} minites, {seconds} seconds.")
    time.sleep(1)
    os.system("cls")
    
    