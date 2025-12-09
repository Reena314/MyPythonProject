 # multilevel inheritance with staticmethod

class Animal: 
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)
 

class Pet(Animal):
    def __init__(self, name, color):
        super().__init__(name)       # call parent (Animal) constructor
        self.color = color

    def show(self):
        print("Name:", self.name, "Color:", self.color)


class Dog(Pet):
    # def __init__(self, name, color, sound):
    #     super().__init__(name, color)   # call parent (Pet) constructor
    #     self.sound = sound
       
       @staticmethod             # because i dont want to use self
       def bark():
        print("Sound:", "bow bow")


# Create object
d = Dog("Rozy", "Brown")

# Call methods
d.show()   # from Pet
d.bark()   # from Dog

# access variable directly (✅ without parentheses)
print("Dog's name:", d.name)
