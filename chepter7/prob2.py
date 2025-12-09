#  wap to greet all the persons name stored in a list l , which are starting with s
l = ["kiran", "rahul", "sachin","sanam"]
for name in l:
    if name.startswith("s"):
        print(f"hello { name }")
        #  print("hello , "+ i)   f string is used for this