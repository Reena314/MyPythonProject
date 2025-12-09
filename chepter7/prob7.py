#wap to multiplication  table of given number using for loop in reverse order
n = int(input("enter a number : ", ));
for i in range(1, 11):
    print(f"{n}*{11-i} = {n*(11-i)}")
