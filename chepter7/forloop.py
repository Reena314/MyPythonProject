# for loop
i = 0
for i in range(10):
    print(i)
    
# for loop for list
list = ["karan", "kamal", "frana", "rohit", "parmeet"]
for i in list:
    print(i)

#for loop for tuple
t = (1, 34,56,78)
for i in t:
    print(i)

 # for loop for string
s = "kiran"
for i in s:
    print(i)
    
   
 # for loop for (start stop step_size)
print("start stop step_size")     
for r in range(2,10,2):
        print(r)

# for loop with else
#print("for loop with else")
e = (1, 7,8)
for i in e:
    print(i)
else:
    print("done")        

# break in for loop
b = (1, 2, 3, 4, 5)
for i in b:
   
    if i==4:
        break
    print(i)


# continue in for loop
print("continue in for loop")
c = range(30)
for i in c:
    if i==20:
        continue   # skip 20 and next continue
    print(i)

# pass in for loop

for i in range(10):
    pass      # do nothing but skip this iteration and go to next with pass

i = 0
while(i<6):
    print(i)         # this work after using pass
    i+= 1