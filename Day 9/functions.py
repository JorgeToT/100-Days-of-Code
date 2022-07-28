import os


def give_name_bid(dict):
    name = input("Name of the person: ")
    bid = int(input("Bid: $"))
    dict[name] = bid


def biggest_bid(dic_of_bids):
    value = 0
    for key in dic_of_bids:
        if dic_of_bids[key] > value:
            value = dic_of_bids[key]
            person_biggest_bid = key
    print(
        f"The biggest bid was from {person_biggest_bid} for ${dic_of_bids[key]}")


def more_bids(answer, dic_of_bids):
    if answer == "Y":
        _ = os.system('cls')
    elif answer == "N":
        biggest_bid(dic_of_bids)
    else:
        print("Invalid argument. Exit from game.")
