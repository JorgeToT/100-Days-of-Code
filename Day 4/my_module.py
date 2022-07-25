import random

pi = 3.14159246


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

# Write your code below this line 👇
    selection = int(input(
        "What do you choose? 1 for Rock, 2 for Paper, 3 for Scissors: \n"))
    computer_selection = random.randint(1, 3)
    images = [rock, paper, scissors]
    print(f"\nYour choice:\n{images[selection - 1]}\n")
    print(f"Computer choice:\n{images[computer_selection - 1]}\n")
    if selection == computer_selection:
        print("It's a tie!")
    elif selection == 1 and computer_selection == 2:
        print("You lose!")
    elif selection == 2 and computer_selection == 3:
        print("You lose!")
    elif selection == 3 and computer_selection == 1:
        print("You lose!")
    else:
        print("You win!")
