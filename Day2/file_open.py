#The Open function takes two parameter: filename, mode.
#The four diffent Mode:
    #"r"=> Opens file for reading.
    #"a"=> Opens file for appending, creates the file if doesn't exists.
    
    #"w"=> Opens file for writting, creates the file if does not exist.
    #"x"=> Creates a specified file.
    
import os   
print(os.getcwd())
# print(os.listdir())

# f=open("Day2/demo.txt", "r")
# print(f.read())
# f.close()


#with...as automatically handles opening and closing the file for you. This provides us cleaner code & Error Handling

def SaveChatMessage(user,message):
    with open("Day2/demo.txt","a") as chat_file:
        chat_file.write(f"{user}: {message}\n")
        
        
def readFromFile():
    with open("Day2/demo.txt") as chat:
        return chat.read()
        
SaveChatMessage("Shanto","Welcome to Our Python Tutorial")
SaveChatMessage("Shanto","You have to focus your goal")


print("\n\n")
print(readFromFile())