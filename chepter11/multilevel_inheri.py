class employee:
    company = "microsoft"
    name = "rahul"
def show(self):
    print(f"my name is : {self.name} and my company name is : {self.company}")

class programmer(employee):
        language = "python"
        def showlanguage(self):
            print(f"my language is : {self.language}")

class team(programmer):
    address = "Lucknow"
    def showaddress(self):
        print(f"my name is : {self.name} and my address is : {self.address} my language is : {self.language}")

t = team()
t.showaddress()


#or   for inherit methods use super()

class employee1:
    def __init__(self, company):
        self.pcompany = company
    def show1(self):
        print(f"my company name is : {self.pcompany}")

class coder(employee1):
    def __init__(self, company, language):
     super().__init__(company)
     self.clanguage = language
    def showlanguage(self):
        print(f"my language is : {self.clanguage}")
class teamlead(coder):
    def __init__(self, company,language, teamsize):
        super().__init__(company,language)
        self.teamsize = teamsize
    def showteamsize(self):
            print(f"my team size is : {self.teamsize} and \n my language is : {self.clanguage} and \n my company name is : {self.pcompany}")

team = teamlead("google", "python", 10)
team.showteamsize()
team.show1()
team.showlanguage()




    
    