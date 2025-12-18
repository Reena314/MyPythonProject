# wap to wipe out the content of a file

with open("../write.txt", "w") as f:
    f.write("")




    

# wap to rename a file with "rename_by_python"

with open("oldfile.py" , "r") as f:
   content = f.read()
   with open("rename_by_python.py" , "w") as f:
      f.write(content)


      #or

      import os

# Rename a file
os.rename("oldfile.py", "rename_by_python.py")

print("File renamed successfully!")
