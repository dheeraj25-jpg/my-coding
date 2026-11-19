# Python Number Guessing Game

import random

# Create Game Function
def guessing_game():

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:

        guess = int(input("\nEnter Your Guess: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("Too Low! Try a Higher Number.")

        elif guess > secret_number:
            print("Too High! Try a Lower Number.")

        else:
            print("\nCongratulations! You Won!")
            print("Correct Number:", secret_number)
            print("Total Attempts:", attempts)
            break


# Main Program
while True:

    guessing_game()

    play_again = input("\nDo You Want to Play Again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\nThank You for Playing!")
        break