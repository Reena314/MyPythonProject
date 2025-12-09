# wap to print third, fifth and seventh element from the list using enumerate

mylist = [1,2,3,4,5,6,7,8,9,10]

for index, item in enumerate(mylist):
    if index == 2 or index == 4 or index == 6:
        print(item)