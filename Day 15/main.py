import data
import functions
StateOfMachine = True


def main():
    initAnswer = input(
        "\nWhat would you like? (Espresso | Latte | Cappuccino) ").lower()
    StateOfMachine = functions.firstAnswer(initAnswer, data.resources)
    return StateOfMachine


while StateOfMachine:
    StateOfMachine = main()
