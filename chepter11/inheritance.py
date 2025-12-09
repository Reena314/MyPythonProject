# Inheritance allows one class (child) to use the properties and methods of another class (parent).
''' 
This helps you:

Reuse code

Avoid repetition

Build relationships between classes 

'''

class employee:
    def __init__(self, company):
       self.company = company
    def display(self):
        print("Company:", self.company)
    
# class programmer:
#     def __init__(self,company):
#        self.company = company
#     def show(self):
#         print("Company:", self.company)
    #or
class programmer(employee):       # copy constructor of employee class
    def __init__(self,company):
       self.company = company
    def show(self):
        print("Company:", self.company)

e1 = employee("microsoft")
e1.display()
p1 =  programmer("google")
p1.show()

# to solve this repitation and reusability we use inheritance


class employee:
    company = "microsoft"
    def display(self):
        print("Company:", self.company)
    
class programmer(employee):
    company = "google"
    language = "python"
    def showlanguage(self):
        print("Company:", self.company + "Language", self.language)

e = employee()
p = programmer()
print("new : ", e.company, p.company , p.language)




#so we create a parent class and child class

class Employee:
    def __init__(self, company):
       # self.company = company
        self.project_company = company   # name change because  if i want change company name 

    def display(self):
        print("Company:", self.project_company)


class Programmer(Employee):
    def __init__(self, company, language):
        # call parent class constructor
        super().__init__(company)         
        self.language = language

    def show(self):
        print(f"I work at {self.company} and my programming language is {self.language}")


# Create object of Programmer
p1 = Programmer("Google", "Python")

p1.company = "Microsoft"        # instance attribute change
p1.display()  # inherited from Employee
p1.show()     # defined in Programmer

    

    