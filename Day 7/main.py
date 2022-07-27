import random
import stages

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6

display = ["_" for letter in range(len(chosen_word))]
print(stages.tittle)
print("Welcome to Hangman Game")
print(f"{stages.stages[lives]}")

while display != list(chosen_word):
    guess = input("Guess a letter: ").lower()

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = chosen_word[letter]
            if display == list(chosen_word):
                print("You win!")
                break

    if chosen_word.find(guess) == -1:
        lives -= 1
        print(f"{stages.stages[lives]}")
        if lives == 0:
            print("You lose!")
            break

    print(''.join(display))
