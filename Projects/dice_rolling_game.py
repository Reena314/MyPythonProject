import random
#playing = True
# while playing:
while True:
    dice = input("Roll The Dice (y/n) : " ).lower()
    if dice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"{dice1} , {dice2}")
    elif dice == 'n':
        print("thank you for palying")
        break;
    else:
        print("invalid value")
    

    
    
