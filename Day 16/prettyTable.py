from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Pokemon name", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Charmander", "Fire"],
        ["Squirtle", "Water"],
        ["Bulbasaur", "Grass"],
    ]
)
x.align = "l"

print(x)
