

# self refers to the current instance of the class.

# It’s used to access variables and methods that belong to the same object.

# It is automatically passed when you call a method on an object.

#  need  of self to access the attributes of class and methods of class 


class person:

    name = "kritika"
    age = 33
    address = "Lucknow"

    def getdata(self):     # if we remove self then it will throw error
     print(f"the name of the person is :{self.name} and age is : {self.age}")


p1 = person()
# p1.getdata()
# or
person.getdata(p1)      # same as p1.getdata()

# or
# multiple objects in same class and using self to access the attributes of class and methods of class 
      
class employee:
    def __init__(self, company, salary):
     self.company = company
     self.salary = salary

    def getdata(self):      #अगर self नहीं होगा, तो Python को पता ही नहीं चलेगा कि कौन-सा object method चला रहा है।
        print(f"the company name is :{self.company} and salary is : {self.salary}")

e1 = employee("google", 200000)
e2 = employee("microsoft", 300000)
e1.getdata()
e2.getdata()

# if we have one object and two diffrent methods

class student:
    name = "karan"
    age = 20
    def getinfo(self):      # instance method
        print(f"the name of the student is :{self.name} and age is : {self.age}")
    def greet(self):
        print("hello")

s1 = student()
s1.greet()
s1.getinfo()




