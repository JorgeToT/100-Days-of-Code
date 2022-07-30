def difficulty(selected_difficulty):
    lives = {
        "easy": 10,
        "hard": 5
    }
    if selected_difficulty in lives:
        return lives[selected_difficulty]


def guess_the_num(num_system, num_player, lives):
    if num_system > num_player:
        print("Wrong!\nToo low your number.")
        lives -= 1
        return lives
    elif num_system < num_player:
        print("Wrong!\nToo high your number")
        lives -= 1
        return lives
    elif num_player == num_system:
        return -1
