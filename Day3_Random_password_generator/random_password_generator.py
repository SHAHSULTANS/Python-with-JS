
import random 
import string

#help(random)
#print(string.ascii_lowercase)


def generate_password(length=8,use_uppercase=True,use_lowercase=True,use_number=True,use_special=True):
    #"""Generate a random passoword based on user preference."""
    characterPoll=""
    
    if(use_uppercase):
        characterPoll+=string.ascii_uppercase
    if(use_lowercase):
        characterPoll+=string.ascii_lowercase
    if(use_number):
        characterPoll+=string.digits
    if(use_special):
        characterPoll+=string.punctuation
        
        
    if(not characterPoll):
        raise ValueError("At least one character type must be selected.")
        
        
    passowrd=""
    passowrd="".join(random.choice(characterPoll) for _ in range(length))
    # for x in range(0,length,1):
    #      passowrd+=random.choice(characterPoll)
    
    return passowrd
    
   
   
   
   

def main():
    print("Welcome to the Password Generator")
    length=int(input("Enter the desired length of the password: ")) 
    
    uppercase=input("Include uppercase letters? (y/n): ").strip().lower()=="y"
    lowercase=input("Include lowercase letters? (y/n): ").strip().lower()=="y"
    numbers=input("Include numbers? (y/n): ").strip().lower()=="y"
    specialChar=input("Include specialChar=? (y/n): ").strip().lower()=="y"
    try:
        ans=generate_password(length,uppercase,lowercase,numbers,specialChar)
        print(ans)
    except ValueError as e:
        print(f"Error: {e}")
        
    

    
if __name__=="__main__":
    main()
    