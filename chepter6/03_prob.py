# show spam comments

p1 = "you got a job offer"
p2 = "your loan is approved"
p3 = "you won a lottery"
p4 = "your mobile is haked"

comment = input("enter your comment : ")
if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("this is spam message")
else:
    print("this is not spam message")
    