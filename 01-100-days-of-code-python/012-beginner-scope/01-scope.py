# Scope

enemies = "Skeleton"


def increase_enemies():
    enemies = "Zombie"  # Create new variable not same as enemies from global scope
    print(f"enemies inside function: {enemies}")


increase_enemies()  # -> Zombie
print(f"enemies outside function: {enemies}")  # -> Skeleton


# Local Scope
def drink_potion():
    potion_strenght = 2  # local variable in local function scope

    def print_strenght():  # local function in local function scope
        print(potion_strenght)  # potion_strenght is visible in every inner scopes

    print_strenght()


# print_strenght() # Not accessible out of drink_potion() scope
# print(potion_strenght) # Not accessible out of drink_potion() scope


# Global Scope
player_health = 10


def print_health():
    print(f"inside print_health(), player_health = {player_health}")


print_health()
print(f"outside print_health(), player_health = {player_health}")

# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

# Possibly unbound (if false will not create new_enemy and we will get error)
# Example is from tutorial, comments from me
print(new_enemy)
