
import random

def roll_dice():
    number = random.randint(1, 6)
    print("You rolled the die and got ...", number)

def main():
    while True:
        print("1. Roll the dice\n2. Exit")
        user_choice = input("What do you want to do? ")
        if user_choice == "1":
            roll_dice()
        elif user_choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
