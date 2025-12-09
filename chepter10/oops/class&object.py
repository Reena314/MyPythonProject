# class is a blueprint of creating objects
# class define the properties and methods of object
# class is a placeholder for creating objects

class Employee:
     ename = "rehana"
     age = 21                              # properties of class or attributes
     language = "english"
     salary = 20000

rehana = Employee()     # object of class
print(rehana.ename,rehana.age,rehana.language,rehana.salary) # access the properties of object

#or
# object is an instance of class 
class student:
     
     age = 21                              # properties of class or attributes
     language = "english"
     fee = 20000

kiran = student()     # object of class
kiran.name = "kumari"   # add new property to object and its called instance variable and name is a object attribute
print(kiran.age,kiran.language,kiran.fee, kiran.name)
