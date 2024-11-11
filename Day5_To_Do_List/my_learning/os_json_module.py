
import os
import json

PathName="Day4_To_Do_List/my_learning/test.json"

print(os.path.exists(PathName))
print(os.name)

def PathExist():
    if(os.path.getsize(PathName)==0):
        return[]
    
    with open(PathName,"r") as f:
        return json.load(f)
        
        
if(os.path.exists(PathName)):
    store=PathExist()
    # print(store)
    store.append({"name":"Shanto"})
    # print(store)
    with open(PathName,"w") as f:
        json.dump(store,f)
        
    for x in store:
        print(x["name"])
    
    
