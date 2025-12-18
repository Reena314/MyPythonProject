# WAP to remove a word from a list and strip that word from the remaining items

l = ["karan", "kamal", "frana", "arohita", "parmeet", "al"]

def rem(l, word):
    new_list = []                     # new list to store final result
    for item in l:
        if item == word:              # if item is exactly the word to remove
            continue                  # skip it (do not add in new list)
        cleaned = item.replace(word, "")   # remove word from inside the item
        new_list.append(cleaned)      # add cleaned item to new list
    return new_list

print(rem(l, "al"))
