from random import randint

system = randint(1, 10)
guesses = 1
user_choice = 0

while(system != user_choice):
    user_choice = int(input("Enter your choice: "))
    if(system > user_choice):
        print("Your guess is too low")
        guesses += 1
    elif(system < user_choice):
        print("Your guess is too high")
        guesses += 1

print(f"Your guess is correct in {guesses} attempts.")
