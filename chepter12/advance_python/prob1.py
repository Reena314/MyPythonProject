# wap to open the three files 1.txt, 2.txt, 3.txt and if any these files are not present then a message without exiting the program .
try:
    with open("1.txt", "r") as f1:
      f1.read()
except Exception as e:
    print("file not found")

        
try:
    with open("2.txt", "r") as f2:
      f2.read()
except Exception as e:
    print("file not found")


try:
    with open("file2.txt", "r") as f3:
      f3.read()
except Exception as e:
    print("file not found")
else:
    print("file read successfully")

print("program ended")