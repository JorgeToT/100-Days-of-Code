import math


def func_1():
    # Write your code below this line 👇
    def paint_calc(height, width, cover):
        print(f"You'll need {math.ceil((height*width)/cover)} cans of paint.")
    # Write your code above this line 👆
    # Define a function called paint_calc() so that the code below works.
    # 🚨 Don't change the code below 👇
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)


def func_2():
    # Write your code below this line 👇
    def prime_checker(number):
        for i in range(2, number):
            if (number % i == 0):
                return print("It's not a prime number.")
        return print("It's a prime number.")

    # Write your code above this line 👆
    # Do NOT change any of the code below👇
    n = int(input("Check this number: "))
    prime_checker(number=n)


func_2()
