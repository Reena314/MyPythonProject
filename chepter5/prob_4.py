# what will the length of following set
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print((s))       #{'20',20} because of 20 and 20.0 are same
print(len(s))    # 2 because of 20 and 20.0 are same
