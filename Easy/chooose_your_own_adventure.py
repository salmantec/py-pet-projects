name = input("Your name: ")

print(f"Welcome to this adventure game, {name}")

direction_selection = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (type left / right) ? ").lower()

if direction_selection == "left":
    walk_or_swim = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if walk_or_swim == "walk":
        print("You walked for many miles, ran out of water and you lost the game 😔.")
    elif walk_or_swim == "swim":
        print("You swam across and were eaten by an alligator 🐊.")
    else:
        print('Not a valid option. You lose 😔.')
elif direction_selection == "right":
    back_or_cross = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if back_or_cross == "back":
        print("You go back and lose 😔.")
    elif back_or_cross == "cross":
        talk_or_not = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if talk_or_not == "yes":
            print("You talk to the stranger and they give you gold. You WIN! 🏆")
        elif talk_or_not == "no":
            print("You ignore the stranger and they are offended and you lose 😔.")
        else:
            print('Not a valid option. You lose 😔.')
    else:
        print('Not a valid option. You lose 😔.')
else:
    print('Not a valid option. You lose 😔.')

print(f"Thank you for trying {name}")
