# wap  a file contain a word donkey and  replace the word donkey with ###### by updating the same file

f = open("file.txt", "r")
data = f.read()
content = data.replace("donkey","######")
f.close()

with open("file.txt", "w") as f:
    f.write(content)






# a list of such words to be censored
# same in list with multiple words replace  with #



words = ["donkey", "ganda", "nice"]

# Step 1: Read the file
with open("file.txt", "r") as f:
    content_new = f.read()

# Step 2: Replace all listed words
for word in words:
    content_new = content_new.replace(word, "#" * len(word))

# Step 3: Write the updated content once
with open("file.txt", "w") as f:
    f.write(content_new)
