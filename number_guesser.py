import random

max_limit = input("Type a max limit number: ")

if max_limit.isdigit():
    max_limit_to_int = int(max_limit)

    if max_limit_to_int <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, max_limit_to_int)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Try with number")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess < random_number:
        print("You were below the number!")
    else:
        print("You were above the number!")

print(f"You found the number with {guesses} guesses")
