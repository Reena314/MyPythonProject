# wap to create a class "programmer" and storing information of few programmers working of microsoft

class programmer:
    def __init__(self, name, age, salary, company): 
        self.name = name
        self.age = age
        self.salary = salary
        self.company = company

p = programmer("rohit", 21, 200000, "microsoft")
print(p.name, p.age, p.salary, p.company)
p2 = programmer("ranjna", 22, 250000, "microsoft")
print(p2.name, p2.age, p2.salary, p2.company)
