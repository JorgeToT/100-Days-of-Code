from importlib import resources


def firstAnswer(input, resources):
    if input == "off":
        print("Turning off the coffee machine")
        return False
    elif input == "report":
        report(resources)
        return True


def report(resources):
    print(
        f"Report:\n{resources['water']} of water\n{resources['milk']} of milk\n{resources['coffee']} of coffee")
