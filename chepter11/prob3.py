# wa class to add salary and increment to it . write a method salaryAfterIncrement and use property decorator with setter which changes increment based on target salary

class Employee:
    salary = 250       # base salary 
    increment = 10     # default increment %

    @property                             # ✅ Property decorator is used to turn a method into a “read-only” attribute — meaning you can access it like an attribute, but it still runs code behind the scenes (the method).
    def salaryAfterIncrement(self):
        # calculate total salary after applying increment
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # calculate new increment % based on target salary
        self.increment = ((new_salary / self.salary) - 1) * 100


# Create object
e = Employee()

print("Original salary:", e.salary)
print("Default increment:", e.increment)
print("Default salary after increment:", e.salaryAfterIncrement)  # access via property

print("\n--- Now updating salaryAfterIncrement to 300 ---")
e.salaryAfterIncrement = 300  # triggers setter

print("Updated increment:", e.increment)
print("Updated salary after increment:", e.salaryAfterIncrement)
