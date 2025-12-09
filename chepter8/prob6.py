# wap to remove words from a list and strip them at the same time using function

l = ["karan", "kamal", "frana", "arohita", "parmeet", "al"]

def rem(l, word):
 for item in l:
    l.remove(word)
    return l

print(rem(l, "al"))

# or

def rem(l,word):
    n = []         # new list
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n
print(rem(l, "al"))

