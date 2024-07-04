print("Thank you for choosing Python Pizza Deliveries!\n")

print("Small pizza (S): $15")
print("Medium pizza (M): $20")
print("Large pizza (L): $25")
print("")

bill = 0
size = input("What size puzza do you wants (S, M or L)? ")
print("")

if size == "S":
    bill += 15
    print("Add pepperoni for small pizza +$2")
elif size == "M":
    bill += 20
    print("Add pepperoni for medium or large pizza +$3")
else:
    bill += 25
    print("Add pepperoni for medium or large pizza +$3")

add_pepperoni = input("Do you want pepperoni (Y or N)? ")
print("")

print("Add extra cheese for any size pizza +$1")
extra_cheese = input("Do you want extra cheese (Y or N)? ")
print("")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
