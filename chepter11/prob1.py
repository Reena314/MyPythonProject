# create a class (2-D vector) and create another class representing a 3-D vector

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2D vector is {self.i}i + {self.j}j")


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)   # call parent constructor
        self.k = k

    def show(self):   # ✅ Better: same method name for polymorphism
        print(f"3D vector is {self.i}i+{self.j}j +{self.k}k")


# Create objects
v = Vector2D(10, 20)
v.show()

v1 = Vector3D(10, 20, 30)
v1.show()


    