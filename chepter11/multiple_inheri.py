
class employee:
    e_company = "microsoft"
    name = "kiran"

    def show(self):
        print(f"my name is : {self.name} and my company name is : {self.e_company}")

class coder:
    language ="python"
    def showlanguage(self):
        print(f"my language is : {self.language}")

class programmer(employee, coder):
    company = "google"
    def showCompany(self):
        print(f" name is :{self.name} company name is :{self.company}")

p = programmer()
# e = employee()
# c = coder()
# p.showCompany()
# e.show()
# c.showlanguage()
p.show()
p.showCompany()