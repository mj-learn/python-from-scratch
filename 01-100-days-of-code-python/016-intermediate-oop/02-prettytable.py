# Practice Modifying Object Attributes and Calling Methods

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)
