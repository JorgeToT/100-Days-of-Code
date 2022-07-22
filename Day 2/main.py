def sum_two_numbers():
    # 🚨 Don't change the code below 👇
    two_digit_number = input("Type a two digit number: ")
    # 🚨 Don't change the code above 👆

    ####################################
    # Write your code below this line 👇
    print(str(int(two_digit_number[0]) + int(two_digit_number[1])))


def BMI_calculator():
    # 🚨 Don't change the code below 👇
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    BMI = float(weight) / (float(height)*float(height))
    print(int(BMI))


def time_until_90():
    # 🚨 Don't change the code below 👇
    age = input("What is your current age?")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    years = 90 - int(age)
    days = years * 365
    weeks = years * 52
    months = years * 12
    print("You have {days} days, {weeks} weeks, and {months} months left.".format(days=days, weeks=weeks, months=months))


def tip_calculator():
    print("Welcome to the tip Calculator.")
    bill = input("Please enter the total bill amount: $")
    persons = input("How many people to split the bill with? ")
    tip = input("What percentage would you like to tip? 10, 12, 15? ")
    amount = round(float(bill) * (1+float(tip) / 100) / float(persons), 2)
    print("Each person should pay $" + str(amount) + " for a tip.")