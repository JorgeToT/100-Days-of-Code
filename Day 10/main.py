import operations
import logo
import os


def main():
    os.system("cls")
    print(logo.logo)
    still_working = True
    init_num = float(input("What is the first number?\n"))
    while still_working:
        print("\nYou can select the following operations:")
        for symbol in operations.symbols:
            print(symbol)
        operation = input("What operation will you do?\n")
        next_number = float(input("\nWhat is the next number?\n"))
        result = operations.symbols[operation](init_num, next_number)
        print(f"\n{init_num} {operation} {next_number} = {result}\n")
        if input("Wanna continue with the last result (Y), if not (N), you will restart the calculator.").upper() == "Y":
            init_num = result
        else:
            main()


main()
