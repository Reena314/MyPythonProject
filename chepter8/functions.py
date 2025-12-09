# function


def my_function():                     # function definition
  print("Hello from a function")

my_function()        # function call
my_function()
my_function()

# greet with parameter

def greet(name):
  print("good morning:", name)

greet("alice")
greet("nehal")

# get greeting
def get_greeting():
  return "hello everyone"

message = get_greeting()  
print(message)            # if we want to store value in message variable then we use return keyword see above

#or
print(get_greeting())

# add numbers

def add(a, b):
  print(a+b)
  return "add method used"         # return keyword is used to return value from function
sum = add(3,5) 
print(sum)

# fahrenheit to celsius

def fahrenheit_to_celsius(fahrenheit):
 return(fahrenheit-32) * 5 / 9

print(fahrenheit_to_celsius(100))
print(fahrenheit_to_celsius(103))
print(fahrenheit_to_celsius(101))


# Default Parameter values

def default_pmt(name = "friend"):
  print(name)

default_pmt('rekha')
default_pmt("karan")
default_pmt()           # if we not pass any value then it will take default value friend


# for oscar

def oscar(animal,name, age ):
  print("i have " + age + " years old " + animal + " name is " + name )

oscar('dog','oscar','8')

#  sending a list as an argument

def my_fruits(fruits):
  for fruit in fruits:
    print(fruit)
list_fruits = ['apple', 'banana','orange']
my_fruits(list_fruits)

# sending dictionary as an argument

def my_dict(person):
  print("Name : ", person["name"])
  print("Age : ", person["age"] )

person_detail = {'name': 'kunal', 'age': 23} 
my_dict(person_detail) 


#A function that returns a tuple:

def my_tuple():
  return (10,20)

x, y = my_tuple()
print('x :', x)
print('y :', y)
