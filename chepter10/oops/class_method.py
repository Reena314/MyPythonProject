
class person:
    name = "rohan"
    age = 28
    address = "jal"

    @classmethod       #Refers to the class itself, not an instance. and it is class method
    def getinfo(cls):
        print(cls.name,cls.age,cls.address)

person.getinfo()    # 


