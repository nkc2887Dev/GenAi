## ROCK, PAPER, SCISSORS

import random

'''
1 for Rock
2 for Scissors
3 for Paper
'''

system = random.choice([1,2,3])
user = input("Enter your choice: ")
userW = { "r":1, "s":2, "p":3 }

if user not in userW:
    print("Invalid input! Use 'r' for Rock, 's' for Scissors, or 'p' for Paper.")
else:
    convert = { 1: "Rock", 2: "Scissors", 3: "Paper"}
    user_choice = userW[user]

    print(f"system's choice \"{convert[system]}\" And your's \"{convert[user_choice]}\".")
    if system == user_choice:
        print("It's a Draw!")
    elif (user_choice - system) % 3 == 1:
        print("You Win!")
    else:
        print("You Lose!")

    # if(system == 1 and user_choice == 2):
    #     print("You Lose!")
    # elif(system == 1 and user_choice == 3):
    #     print("You Lose!")
    # elif(system == 2 and user_choice == 1):
    #     print("You Win!")
    # elif(system == 2 and user_choice == 3):
    #     print("You Lose!")
    # elif(system == 3 and user_choice == 1):
    #     print("You Win!")
    # elif(system == 3 and user_choice == 2):
    #     print("You Win!")
    # else:
    #     print("Something went wrong!")