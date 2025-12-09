# wa class with a class attribute a, create an object from it and set 'a' directly using object.a=0. Does this change the class attribute

class Demo:
     a = 10

o = Demo()     # object of class
print(o.a)       # access or print  the class attribute because instance attribute is not created
o.a = 0                # instance attribute created
print(o.a)           # print the instance attribute because instance attribute is created
print(Demo.a)      # print the class attribute

# no this does not change the attribute