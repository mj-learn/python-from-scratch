print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print("You're at a cross road. Where do you want to go?")
step_one = input('Type "left" or "right": ').lower()

if step_one == "left":

    print("")
    print("You come to a lake.")
    print("There is an island in the middle of the lake.")
    step_two = input('Type "wait" to wait for a boat or type "swim" to swim across: ').lower()

    if step_two == "wait":

        print("")
        print("You arrive at the island unharmed.")
        print("There is a house with 3 doors. One red, one yellow and one blue.")
        step_three = input("Which colour do you choose (red, blue, yellow)? ").lower()

        print("")

        if step_three == "red":
            print("It's a room full of fire. Game Over.")
        elif step_three == "blue":
            print("You enter a room of beasts. Game Over.")
        elif step_three == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")

    else:
        print("\nYou get attacked by an angry trout. Game Over.")

else:
    print("\nYou fell into a hole. Game Over.")
