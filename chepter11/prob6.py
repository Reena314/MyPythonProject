# write a __str__ method to print the vector following 7i + 8j + 10k
# assume vector of dimensions 3 for this problem

class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j 
        self.k = k
    # def __add__(self, other):
    #     return vector(self.i + other.i, self.j + other.j, self.k + other.k)
    def __str__(self):
        return f"vector {self.i}i + {self.j}j + {self.k}k"

v = vector(7, 8, 10)
print(v)