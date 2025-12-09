
# operator overloading




class operator:
    def __init__(self,n):
        self.n = n
    def __add__(self, num):      
        return self.n + num.n

n = operator(10)
m = operator(20)
print(n + m)     # + is a class operator and it is overloading


# __len__()

class length :
    def __init__(self, name):
     self.name = name
    def __len__(self):
        return len(self.name)
n = length("kritika")
print("length of name is : ", len(n))