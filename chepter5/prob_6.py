# create  an empty dictionary. allow 4 friends  to enter their favourite language as
# values and use keys as their names. assumes names are unique
 
d = {}

name = input("enter your name :")
lang = input ("enter your language :")
d.update({name:lang})  #If a key already exists, its value is overwritten. means update method automatically update key value
name = input("enter your name :")
lang = input ("enter your language :")
d.update({name:lang})
name = input("enter your name :")
lang = input ("enter your language :")
d.update({name:lang})
name = input("enter your name :")
lang = input ("enter your language :")
d.update({name:lang})
print(d)                           # in answer  it shows same name is not allowed but values same are allowed