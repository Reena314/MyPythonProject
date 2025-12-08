expenses = []

def show_expenses():
    print("=======expense Tracker=======")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Show Total Spent")
    print("5. Exit")
    
def addExpense():
    name = input("enter the name of product : ")
    amount = float(input("enter amount of product : ")) 
    category = input("enter the category like: food, shopping,travel etc : ")
    
    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)
    print("expense added")
    
def viewExpense():
    if not expenses:
        print("no expenses recorder yet")
        return
    
    print ("your expenses are : ")
    for e, exp in enumerate(expenses, 1):
            print(f"{e}.{exp['name']}  ${exp['amount']} {exp['category']}")
            
def deleteExpense():
    if not expenses:
        print("no expenses to delete")     
        return
    viewExpense()
    index = int(input("enter number for deletion : "))
    if 1<= index <= len(expenses):
        remove = expenses.pop(index-1)
        print(f"Deleted : {remove['name']} (${remove['amount']}) {remove['category']}")
    else:
        print("invalid number")
        
def totalExpense():
    total = sum(exp['amount'] for exp in expenses)
    print (f"total spent amount : ${total}") 
         
while True :
    show_expenses()
    choice = input("choose an option (1-5) : ")
    
    if choice == "1":
        addExpense()
    elif choice == "2":
        viewExpense()
    elif choice == "3":
        deleteExpense()
    elif choice == "4":
        totalExpense()
    elif choice == "5":
        print("good bye")
        break
    else:
        print("invalid choice")