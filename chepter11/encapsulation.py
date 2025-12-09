# Encapsulation means binding data (variables) and methods (functions) together in a single unit — the class.

#It also helps you hide data from being accessed or modified directly, to protect it from accidental changes.
# Encapsulation = “Data hiding” + “Controlled access”

class employee :
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # private variable

    def show(self):
       print("name : " , self.name)
       print("salary : ", self.__salary)
e = employee("kiran" , 100000)

e.show()


# trying to access salary directly
 # print(e.__salary)                   # it will not access salary directly because it is private variable
                                        # and using double underscore (__)
 #print(e.name)                        # this work

 # remember:
# Python performs name mangling — it changes the variable name internally to something like: _employee__salary
# this prevent private variable from being accessed directly





# Accessing Private Data with Getters and Setters
    

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # getter method
    def get_salary(self):
        return self.__salary

    # setter method
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")

e1 = Employee("Ravi", 50000)
print("Before:", e1.get_salary())   # access via getter

e1.set_salary(60000)                # modify via setter
print("After:", e1.get_salary())

e1.set_salary(-100)                 # invalid



   
    

    
