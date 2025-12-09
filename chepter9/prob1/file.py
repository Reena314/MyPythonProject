# read the text in given file poems.txt and find the word twinkle

f = open("poems.txt", 'r')
data = f.read()
print(data)
f.close()

# or if we find the word in same file and same time 

f = open("poems.txt")
data = f.read()
if ("twinkle" in data):
    print("twinkle is preasent")
else:
    print("twinkle is not preasent")
