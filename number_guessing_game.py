import random

def guess_number():
    
    print("welcome to the guessing number game")
    print(" i am thinking of number between 1 and 100")
    
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    while not guessed : 
        guess = input("enter guessing number : ")
        
        if not guess.isdigit():
           ("please enter a valid number")
           continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("too low ! Try Again ")
        elif guess > number_to_guess:
            print("too high! Try Again")
        else:
            guessed = True
            print(f"congratulation ! you guess the number {number_to_guess} in attempts {attempts}. ")
guess_number()