# using walrus operator

if (n:= len([1,2,3,4,5])) >3:
    print(f"length too long ({n} , expected <=3)")
else:
    print(f"length too short ({n} , expected >=3)")