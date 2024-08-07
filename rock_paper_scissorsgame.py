#ROCK PAPER SCISSORS GAME

import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, and 2 for Scissors  "))

if user_choice >= 3 or user_choice <0:
    print("You enter an Invalid Number, You Loose")

else:

    comp_choice = random.randint(0,2)

    print(comp_choice)

    #print(type(comp_choice))

    if user_choice == comp_choice:

        print("It's a draw")

    elif user_choice > comp_choice:

        print("You win")

    elif comp_choice==0 and user_choice == 2:

        print("You Loose")

    elif comp_choice == 2 and user_choice == 0:

        print("You Win")

    elif comp_choice > user_choice:

        print("You Loose")

