task_list = []

def showMenu():
    print("----To--do---List")
    print("1. view taskList")
    print("2. add task in list")
    print("3. delete task")
    print("4. exit")
    
while True:
    showMenu()
    choice = input("choose an option (1-4): ")
    
    if choice == "1":
        if not task_list:
            print("\n no task")
        else:
            print("\n your task : ")
            for i, task in enumerate(task_list, 1):
             print(f"{i}.{task}")    
    elif choice == "2" :
        task = input("enter new task : ")
        task_list.append(task)
        print("\n task added")
        
    elif choice == "3" :
        if not task_list:
            print("\n no task for deletion")
        else:
          for i , task in enumerate(task_list, 1):
             print(f"{i}.{task}")
        try:                                     # try is uses for when user type unexpected like 3.5
             delete_index = int(input("enter delete number : "))
             if 1<= delete_index <= len(task_list):
              removed = task_list.pop(delete_index - 1)
              print(f"deleted  {removed}")  
             else:
                 print(f"invalid task number")
        except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("\n good bye ")
        break
    else:
        print("\n invalid choice try again")
             
             
        
              
        
      
            
    
