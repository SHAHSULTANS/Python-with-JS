


def greet():
    print("Hello")
    
def main():
    print("This is main")
    greet()
  
#To prevent global function call, if script is imported elsewhere. That means when imported, the main logic doses not automatically execute.
if(__name__=="__main__"):
    main()