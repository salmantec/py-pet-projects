import random

computer_win = 0
user_win = 0
options = ["rock", "paper", "scissors"]

while True:
    user_option = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_option == "q":
        break

    if user_option not in options:
        continue

    # rock - 0, paper - 1, scissors - 2
    random_number = random.randint(0, 2)
    # Computer selection
    computer_option = options[random_number]

    print(f"Computer picked {computer_option}.")

    if user_option == "rock" and computer_option == "scissors":
        print("You won 🥇!")
        user_win += 1
    elif user_option == "paper" and computer_option == "rock":
        print("You won 🥇!")
        user_win += 1
    elif user_option == "scissors" and computer_option == "paper":
        print("You won 🥇!")
        user_win += 1
    elif user_option == computer_option:
        print("Same, try again!")
        continue
    else:
        print("You lost 😩, Computer won 🥇!")
        computer_win += 1

print(f"You won {user_win} times.")
print(f"Computer won {computer_win} times.")
print("Good bye 👋!!")

