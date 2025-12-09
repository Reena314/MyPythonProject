# add static method in class calculator to find square, cube and square root of a number to greet the user with hello

class calculator :
    def __init__(self,num):
        self.num = num
    def square(self):
        print("square is : ", self.num * self.num)
    def cube(self):
        print("cube is :", self.num*self.num*self.num)
    def square_root(self):
        print(f"square_root is :{self.num * 0.5}")

    @staticmethod
    def greet():
        print( "hello ")
c = calculator(3)
c.square()
c.cube()
c.square_root()
c.greet()
