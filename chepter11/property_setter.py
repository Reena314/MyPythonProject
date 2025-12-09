class employee :
    a = 10 
    
    # def show(self):
    #     print("the value of a is :", self.a)
    @classmethod
    def show(cls):
        print("the value of a is :", cls.a)   # result =10

    @property
    def name(self):
          # return self.ename   #property decorator
           #or
           return f"{self.fname} {self.lname}"    # this is used to get the value of the attribute and set property name i.e. fname and lname is a property decorator
    @name.setter
    # def name(self,value):
    #         self.ename = value
       #or
    def name(self, value):
        self.fname = value.split(" ")[0]     # kiran
        self.lname = value.split(" ")[1]       #  when i use name.split(" ") then  it split the name into two parts like kiran and sharma and ['kiran', 'sharma'] so i use fname = name.split(" ")[0] and lname = name.split(" ")[1] to get the first name and last name.




e = employee()
e.a = 20         
e.show()    # result =20 but i want result 10 so i use @classmethod on above method
e.name = "kiran sharma"
print(e.fname)         