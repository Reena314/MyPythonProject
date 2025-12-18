import random

choices = ('r', 'p', 's')
while True :
    user_choice = input("Rock, Paper, Scissor (r,p,s): ").lower()
    # validate input
    if user_choice not in choices:
        print("Invalid value")
        continue

    computer_choice = random.choice(choices)

    # show user choice
    if user_choice == "r":
        print("Rock")
    elif user_choice == "p":
        print("Paper")
    elif user_choice == "s":
        print("Scissor")

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie")
    elif \
        (user_choice == 'r' and computer_choice == 's')or \
        (user_choice == 's' and computer_choice == 'p')or\
        (user_choice == 'p' and computer_choice == 'r'):
        print("you win")
    else :
        print('you lose')
    
    should_continue = input("continue (y/n) : ").lower()
    if should_continue == 'n':
        break;




