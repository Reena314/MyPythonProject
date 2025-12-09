class employee :
    a = 10 
    
    # def show(self):
    #     print("the value of a is :", self.a)
    @classmethod
    def show(cls):
        print("the value of a is :", cls.a)   # result =10

e = employee()
e.a = 20         
e.show()    # result =20 but i want result 10 so i use @classmethod on above method
        