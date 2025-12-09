# Does not take self or cls as a parameter.

# Can’t access instance or class data directly.

# Acts like a normal function, but kept inside a class for logical grouping.

class student:
    name = "mohni"
    age = 18
    s_class = "12th"

    @staticmethod      # not use cls and self . this is work like  normal function

    def stuinfo():
        print("the name of the student is :", student.name, "and age is :", student.age, "and class is :", student.s_class)

student.stuinfo()

# combine example
class Employee:
    company = "OpenAI"

    def __init__(self, name):      # constructor
        self.name = name

    def show(self):                 # Instance method
        print(f"Employee Name: {self.name}")

    @classmethod
    def show_company(cls):          # Class method
        print(f"Company: {cls.company}")        # when we use cls then it will access class attribute not instance attribute

    @staticmethod
    def greet():                    # Static method
        print("Welcome to the company!")

# Usage:
e1 = Employee("Kritika")

e1.show()           # Instance method (uses self)
Employee.show_company()  # Class method (uses cls)
Employee.greet()    # Static method (no self or cls)
