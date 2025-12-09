# the game() in a program lets a user play a game and return the score as an integer.you need to read a file
# highscore.txt which is either blank or contains the previous highscore. you need to write the program to update 
# the highscore whenever the game() breaks the highscore.
import random

def game():
    print("you are playing the game ")
    score = random.randint(1,60)

    with open("highscore.txt", "r") as f:
        hiscore = f.read()
        if hiscore != "":
           hiscore = int(hiscore)
        else:
            hiscore = 0

        print(f"your score is {score} ")

        if (score > hiscore):                        # assume 30>0 
            with open("highscore.txt", "w") as f:
                f.write(str(score))
            return score

game()
