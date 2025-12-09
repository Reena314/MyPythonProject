# write a program to fill in letter template given below with name and date
 # template below 
from os import name


letter = '''Dear <|name|>,
you are perfect,                               
<|Date|>'''

print(letter.replace("<|name|>","Reena").replace("<|Date|>","24 sep 2026"))


           #or way of input
name = input("enter your name :" )
date = input ("enter date (e.g., 2025-10-16): ")
letter_filled = letter.replace("<|name|>", name)
letter_filled = letter_filled.replace("<|Date|>", date)
print("\n letter Filled\n")
print(letter_filled)


        