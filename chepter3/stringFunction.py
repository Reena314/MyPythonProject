string = "rubina "

print(len(string))

print(string.endswith("na")) # endswith blankspace
print(string.startswith("Ru"))  #captalize issues

print(string.capitalize())

a = "Hello, World!  "
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(a.split(","))   # return a list
print(a.find("o"))
print(a.count("o"))
print(a.center(30))   #center the string
print(a.isalpha())
print(a.isdigit())
print(a.islower())
print(a.isupper())
print(a.isnumeric())
print(a.isalnum())
print(a.isdecimal())
print(a.isidentifier())
print(a.isprintable())

print(a.strip())   # remove the leading and trailing spaces

# more functions from chtgpt

age = 36
#txt2 = "My name is John, I am " + age        # error  can only concatenate str (not "int") to str
txt1 = f"My name is John, I am {age}" # formatted string  if f is not use then it print same {age} format not 34
print(txt1)
txt = f"The price is {20 * 59} dollars" 
print(txt)