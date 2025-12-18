def calculate():
   print("-----calculator-----")
   print("1. Add")
   print("2. subtract")
   print("3. divide")
   print("4. multiply")
   print("5. good bye")
   
while True:
       calculate()
       choice = input("choose an option (1-5) : ")
       
       if choice in ["1", "2", "3", "4"]:
           num1 = float(input("enter a number : "))
           num2 = float(input("enter second number : "))
           if choice == "1":
               print(f"Result is : {num1 + num2}")
           
           elif choice == "2":
               print(f"Result is : {num2 - num1}")
           elif choice == "3":
               if num2 == 0:
                   print("error: cannot divided by zero")
               else :
                   
                   print(f"result is : {num1 / num2} ")
           elif choice == "4" :
               print(f"result is : {num1 * num2}")
        
       elif choice == "5" :
        print("good bye") 
        break
       else:
               print("invalid choice") 
                   
                   
            
    
    

