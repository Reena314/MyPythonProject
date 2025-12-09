

class car:
    def __init__(self, name, price, color):  # constructor or also called dunder method which is called automatically
        self.name = name
        self.price = price              # instance variable means it is a variable which is inside a method
        self.color = color
    print("constructor is called")
    def show(self):                    # instance method means it is a method which is inside a class
        print(self.name, self.price, self.color)    # self is a reference variable

c1 =  car("bmw", 200000, "black")     #
c1.show()   

#or

print(c1.name, c1.price, c1.color)





    
   