# wap to find out weather the file is identical and matches the content of another file

with open("../file.txt") as f:
  content =  f.read()

with open("../write.txt") as f:
        content2 = f.read()

        if (content == content2):
            print("files are identical")
        else:
            print("files are not identical")
        

        