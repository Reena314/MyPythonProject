# wap to mine log.txt file and whether it contain python or not




with open("log.txt") as f:
    content = f.read()
    if "python" in content:
        print("python is present")
    else:
        print("python is not present")

# wap to find python line number where pythen is present

with open("log.txt","r")as f :
    linefind= f.readlines()
    line_no = 1
    for line in linefind:
        if "python" in line:
            print(f"python is present in line no: {line_no}")
            break
        line_no += 1
    else:
            print("python is not present in file")