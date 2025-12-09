# wa class to calculator  find the square, cube and square root of a number

class calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
            print( "square is ", self.num * self.num)
    def cube(self):
            print("cube is", self.num * self.num * self.num)
    def square_root (self) :
            print( "square root is",self.num ** 3)

c = calculator(3)
c.square()
c.cube()
c.square_root()   


#or 

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num ** 3}")

    def square_root(self):
        print(f"Square root of {self.num} is {self.num ** 0.5}")

# Create object with a number
c = Calculator(3)

# Call methods
c.square()
c.cube()
c.square_root()


