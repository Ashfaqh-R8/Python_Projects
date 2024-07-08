import random
import os


def toss_coin():
    list1 = ["heads", "tails"]
    return random.choice(list1)


def main():
    while True:
        flag = False  #to break out of 2 nested while loops
        os.system("cls")

        answer = input("Pick a side for the coin toss (heads/tails): ")
        list= ["heads", "tails"]
        if answer.lower() not in list:
            continue

        result = toss_coin()

        print(f"You got ... {result}")

        if answer.lower() == result:
            print("Wow, You won, You're a lucky one")
        else:
            print("OOPS. Better luck next time pal. Try again")

        while True:
            answer_y = input("Wanna play again? (yes/no): ")
            if answer_y.lower() == "no":
                flag = True
                break
            elif answer_y.lower() == "yes":
                break  
            else:
                continue

        if flag:  # Check if flag is True
            break


if __name__ == "__main__":
    main()