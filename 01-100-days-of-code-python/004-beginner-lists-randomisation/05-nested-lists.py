fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Spinach",
    "Cherries",
    "Pears",
]

vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes",
]

# Make list with lists
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# print first item from the first list in dirty_dozen
print(dirty_dozen[0][0])

# print last item from last list in dirty_dozen
print(dirty_dozen[-1][-1])
