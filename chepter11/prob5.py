# wa class vector repersenting a vector of n dimensions. overload the + and * operator which calculate the sum and dot(.) product of them

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):     # dunder method
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):  # dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):     # this method is used if output show like <__main__.Vector object at 0x722768138aa0>
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"  

    def __len__(self):
        # length using ** operator instead of math.sqrt
        return int((self.x**2 + self.y**2 + self.z**2) ** 0.5)

# Example
v = Vector(1, 2, 3)
v1 = Vector(4, 5, 6)
v2 = Vector(7, 8, 9)
print("Addition:", v + v1)
print("Dot Product:", v * v1)
print("Length of v:", len(v))




