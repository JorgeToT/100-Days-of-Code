############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import os
import art
import functions


def main():
    os.system('cls')
    print(art.logo)
    user, dealer = [functions.give_card(), functions.give_card()], [
        functions.give_card(), functions.give_card()]
    print(
        f"\nHere your cards: {user}\nHere dealer's cards: {[dealer[0], '?']}")

    user = functions.stand_or_hit(user)
    sum_user = sum(user)
    if sum_user > 21:
        print(f"\nYour sum is {sum_user}\nYou lose!")
        if functions.play_again():
            main()
        else:
            return

    dealer = functions.check_dealer_sum(dealer)

    sum_dealer = sum(dealer)

    print(
        f"\nYour cards: {user}\nThe sum is {sum_user}\n\nDealer's cards: {dealer}\nThe sum is {sum_dealer}")
    if sum_dealer > 21 or sum_user > sum_dealer:
        print("\nYou win!")
    elif sum_user == sum_dealer:
        print("\nDraw!")
    else:
        print("\nYou lose!")

    if functions.play_again():
        main()
    else:
        return


main()
