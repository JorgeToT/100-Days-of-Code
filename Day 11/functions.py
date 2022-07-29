import random


def give_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards))-1]


def stand_or_hit(player):
    if sum(player) > 21:
        return player
    answer = input("\nWanna stand (S) or hit (H)?\n").upper()
    if answer == 'H':
        player.append(give_card())
        player = as_draw(player)
        print(f'Your cards: {player}')
        stand_or_hit(player)
    return player


def check_dealer_sum(dealer):
    if sum(dealer) < 18:
        dealer.append(give_card())
        dealer = as_draw(dealer)
        check_dealer_sum(dealer)
    return(dealer)


def as_draw(player):
    if sum(player) > 21:
        if 11 in player:
            player[player.index(11)] = 1
            as_draw(player)
    return player


def play_again():
    if input("\nWanna play again?(Y or N)\n").upper() == "Y":
        return True
    else:
        return False
