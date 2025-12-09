mylist = [1,2,3,4,5]

#squaredList =[]

# for item in mylist:
#     squaredList.append(item*item)
# print(squaredList)

#or

squaredList=[i*i for i in mylist]
print(squaredList)

even_squares = [i * i for i in range(10) if i % 2 == 0]
print("even squares: ", even_squares)



