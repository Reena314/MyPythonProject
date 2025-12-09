# write a python program to display a user enter name followed by Good afternoon using input() function

name1 = input("enter your name : ")
print("good afternoon " +  name1)



# not use input() 

name = "kiran sharma"

print("good afternoon {name}") # print {name} because f string is not use

print(f"good afternoon {name}") # using f string
print("good afternoon "+name+" ")  # old method