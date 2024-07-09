# A small project of Rock, Paper and Scissor game developed using python

import random

print("GAME NAME - Rock, Paper and Scissor")
print(
    "GAME RULES :\n--> Choose r for Rock, p for Paper and s for Scissor\n--> If any game draws, it'll be counted\n--> If you pressed other than s, w and g key, it'll be counted."
)
print('\n')
ready = input(
    "So, Be ready the game is starting\n=========Press Enter to start=========\n"
)

totalchances = 3
user_score = 0
computer_score = 0
gameno = 0

lst = ["r", "p", "s"]
print("[ r ] - Rock\n[ p ] - Paper\n[ s ] - Scissor\n")

while gameno < totalchances:
    gameno = gameno + 1
    print(f"=========Game {gameno} is starting=========")

    user = input("CHOOSE WISELY:= ")
    computer = random.choice(lst)

    if user == "r" and computer == "r":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "r" and computer == "s":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "r" and computer == "p":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "p" and computer == "p":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "p" and computer == "s":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "p" and computer == "r":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "s" and computer == "s":
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Match Draw !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "s" and computer == "p":
        user_score = user_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! You WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    elif user == "s" and computer == "r":
        computer_score = computer_score + 1
        print(f"Your Choice = {user} and Computer Choice = {computer}")
        print("!!! Computer WON !!!")
        print(f"===> Youe Score: {user_score}")
        print(f"===> Computer Score: {computer_score}")

    else:
        print("(*)---Please choose correct option---(*)")

print("|*|*|*|*|*|*|*| GAME OVER |*|*|*|*|*|*|*|")
print(
    "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
)
print(
    f"Your Total Score is : {user_score} and Computer's Total Score is : {computer_score}"
)
if user_score > computer_score:
    print(
        "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    )
    print(
        "Hurrey!!! You Won the Series\nHere is a gift for you.... ❤❤❤🎂🎂🎂\nSee you next time.Bye......"
    )
else:
    print(
        "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    )
    print(
        "Sorry!!! You lose the series\nDon't worry you'll still get a gift.... 😝LOL😝 Come next time "
    )

out = input("<=== Press any key to exit ===>")