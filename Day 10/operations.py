from audioop import mul


def sum(a, b):
    return a+b


def mult(a, b):
    return a*b


def div(a, b):
    return a/b


def rest(a, b):
    return a-b


symbols = {
    "+": sum,
    "-": rest,
    "/": div,
    "*": mult
}
