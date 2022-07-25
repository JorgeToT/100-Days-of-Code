import random
import my_module


def random_int():
    random_int = random.randint(1, 100)
    print(random_int)


def random_float():
    random_float = random.random() * 5
    print(random_float)


def pi():
    print(my_module.pi)


def tail_or_head():
    # 🚨 Don't change the code below 👇
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    # 🚨 Don't change the code above 👆 It's only for testing your code.

    # Write the rest of your code below this line 👇
    result = random.randint(0, 1)
    if result == 1:
        print("Heads")
    else:
        print("Tails")


def prepare_the_dinner():
    # 🚨 Don't change the code below 👇
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)

    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    name = names[random.randint(0, len(names) - 1)]
    print(f"{name} is going to buy the meal today!")


def treasure_map():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇
    map[int(position[1])-1][int(position[0])-1] = "X"
    # Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")


my_module.rock_paper_scissors()

