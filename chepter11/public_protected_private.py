  
class coder :
    def __init__(self):
        self.name = "radha"             # public
        self._project = "microsoft"     # protected
        self.__revenue = "10m"          # private

    def show(self):
            print("name :", self.name)
            print("project :", self._project)
            print("revenue :", self.__revenue)

c = coder()
c.show()
print(c.name)       # ✅ public - accessible
print(c._project)    # ⚠️ possible, but not recommended
print(c.__revenue)   # ❌ error (private)
    