#write a program to find the percentage of student and check user is pass or fail using user input.
#  Assume 3 subjects marks and user enter marks

marks = int(input("enter marks1 : "))
marks2 =int(input("enter marks2 : "))
marks3 =int(input("enter marks3 : "))

percentage = (100*(marks + marks2 + marks3)) / 300

if (percentage >=40 and marks>=33 and marks2>=33 and marks3>=33):
    print("pass", percentage)
else:
    print("fail", percentage)
