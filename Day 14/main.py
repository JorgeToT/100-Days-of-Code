import os
import art
import game_data
import random


def show_options(data, prev):
    option_2 = random.randint(0, len(data)-1)
    if prev == option_2:
        show_options(data)
    print(
        f"Option A: {data[prev]['name']}, a {data[prev]['description']}, from {data[prev]['country']}")
    print(art.vs)
    print(
        f"\nOption B: {data[option_2]['name']}, a {data[option_2]['description']}, from {data[option_2]['country']}\n")
    return prev, option_2


def is_correct(option_1, option_2, data):
    option_1_count = data[option_1]["follower_count"]
    option_2_count = data[option_2]["follower_count"]
    if option_1_count > option_2_count:
        return option_1
    elif option_2_count > option_1_count:
        return option_2


def main(data):
    os.system('cls')
    print(art.logo)
    score = 0
    still_playing = True
    prev = random.randint(0, len(data)-1)
    while still_playing:
        print(
            f"----------------------------------\nYour current score is {score}\n")
        a, b = show_options(data, prev)
        answer = input(
            "Who has more followers on Instagram? (A or B)\n").upper()
        correct = is_correct(a, b, data)
        if answer == 'A' and correct == a:
            print("Is's correct\n")
            score += 1
            prev = a
        elif answer == 'B' and correct == b:
            print("Is's correct\n")
            score += 1
            prev = b
        else:
            if input("\nYou lose.\nWanna play again? (Y or N)\n").upper() == "Y":
                main(data)
                return
            else:
                still_playing = False
    print("Bye! Good Game\n")
    return


main(data=game_data.data)
