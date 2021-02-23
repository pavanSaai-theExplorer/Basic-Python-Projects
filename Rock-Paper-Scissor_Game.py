    # Rock - Paper - Scissors Game (User VS Computer)

    # Importing random and time Modules

import random
import time

# Printing Game Rules

print(" Game Winning Rules : \n\n"
      + "Rock  VS Paper   -- >  Paper Wins \n"
      + "Rock  VS Scissor -- >  Rock Wins  \n"
      + "Paper VS Scissor -- >  Scissor Wins \n")

while True:
    print("Enter your Choice \n 1 for Rock \n 2 for Paper \n 3 for Scissors")

    # Taking User Input

    choice = int(input("Please Enter your Choice : "))

    # Looping until user enter Valid Input

    while choice > 3 or choice < 1:
        choice = int(input("Please Enter valid Input : "))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print("\n User Choice : " + user_choice)

    # Using randint method of random module

    comp_choice = random.randint(1, 3)

    # Looping until comp_choice value is equal to choice value

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        computer_choice = "Rock"
    elif comp_choice == 2:
        computer_choice = "Paper"
    else:
        computer_choice == "Scissor"

    time.sleep(1.5)

    print(" My(Computer) Choice : " + computer_choice)

    print("\n ..." + user_choice + " VS " + computer_choice + "... \n")

    # Winning Condition

    if((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):

        time.sleep(1.5)

        print("Winner is Rock ! \n\n", end="")
        result = "Rock"
    elif((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):

        time.sleep(1.5)

        print("Winner is Paper ! \n\n", end="")
        result = "Paper"
    else:

        time.sleep(1.5)

        print("Winner is Scissor ! \n\n", end="")
        result = "Scissor"

    # Printing whoever wins the game

    if result == user_choice:
        print("*** User Wins *** \n")
    else:
        print("*** I(Computer) Won..! *** \n")

    # Calling sleep function

    time.sleep(1)

    print("Do you wanna play again..!  (Y/N) ")
    answer = input()

    # Coming out of the game if user is not interested

    if answer == "N" or answer == "n":
        break

print("\n Hope You enjoyed the game ..!"
          "\n Thanks! for having fun with me ...")
