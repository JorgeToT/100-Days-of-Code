# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import logo
import os
import random
import functions


def main():
    os.system("cls")
    print(logo.logo)
    number_of_tries = functions.difficulty(
        input("Write the difficulty of the game. (Easy or Hard)\n").lower())
    number_to_guess = random.randint(1, 100)
    while number_of_tries > 0:
        number_player = int(
            input(f"\nYou have {number_of_tries} attempts left.\nMake a guess:\n"))
        number_of_tries = functions.guess_the_num(
            num_system=number_to_guess, num_player=number_player, lives=number_of_tries)
        if number_of_tries == -1:
            print(
                f"\nYou guess it, {number_to_guess} is the number I was thinking.\nYou win!")
            answer = input("\nWanna play again? (Y / N)").upper()
            if answer == "Y":
                main()
            else:
                return print("Bye!")
    print(
        f"\nYou lose!\nThe number {number_to_guess} was the number that you have to guess.")
    answer = input("\nWanna play again? (Y / N)").upper()
    if answer == "Y":
        main()
    else:
        return print("Bye!")


main()
