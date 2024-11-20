
import json
from datetime import datetime
import os


TASK_FILE="Day5_To_Do_List/task.json"

def load_tasks():
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE,"r") as file:
            return json.load(file)
    
    return []


def saveTask(tasks):
    with open(TASK_FILE,"w") as file:
        json.dump(tasks,file,indent=4)
      
      
def view_tasks(tasks):
    if not tasks:
        print("NO task available")
    else:
        print("\n"+"="*30+ " TO-DO LIST " + "="*30)
        for index,task in enumerate(tasks, start=1):
            status="✓" if task["completed"] else "✗"
            print(f"\n\nTask #{index}")
            print(f"Title      : {task["title"]}")
            print(f"Category   : {task['category']}")
            print(f"Priority   : {task['priority']}")
            print(f"Due Date   : {task['due_date']}")
            print(f"Status     : {status}")
    print("\n" + "="*70)


def add_task(tasks):
    title=input("Enter the task title: ").strip()
    category=input("Enter task category (e.g., Work, Personal): ").strip()
    
    priority=input("Enter task priority (Low, Medium, High): ").strip().capitalize()
    
    while priority not in ["Low","Medium","High"]:
        print("Invalid priority. Please enter Low, Medium, or High.")
        priority = input("Enter task priority: ").strip().capitalize()
        
        
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        
        
    try:

        due_date=datetime.strptime(due_date,"%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Setting due date to 'No deadline'")
        due_date="No date"
    
    tasks.append({
        "title":title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })    
    # print(tasks)
    saveTask(tasks)
    
        
        
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        tasks[task_num-1]["completed"]="✓"
        saveTask(tasks)
    except(ValueError,IndexError):
        print("Invalid task number? try again")   
    

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        task= tasks.pop(task_num-1)
        print(f"\nTask '{task['title']}' deleted successfully!\n")
        saveTask(tasks)
    except(ValueError,IndexError):
        print("Invalid task number? try again")   
    

def main():
     tasks=load_tasks()
     while True:
        print("\n" + "="*30 + " TO-DO LIST MENU " + "="*30)
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Mark a task as complete")
        print("5. Exit")
        print("="*70)
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice=="3":
            delete_task(tasks)
        elif choice=="4":
            complete_task(tasks)
        else:
            print("Invalid key? choice again!")
            
            
   
    # print(tasks)
    
    # add_task(tasks)
    




if __name__=="__main__":
    main()