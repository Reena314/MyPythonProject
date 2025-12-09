# write a program to find the user input name in post

post = input("enter post : ")

if("karan".lower() in post.lower()): # it convert all the characters to lower case
    print("karan is in post")
else:
    print("karan is not in post")