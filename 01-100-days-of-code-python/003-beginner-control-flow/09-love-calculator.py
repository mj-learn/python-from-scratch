print("The Love Calculator is calculating your score...\n")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
print("")

true_total = 0
love_total = 0

both_names = name1.lower() + name2.lower()

true_total += both_names.count("t")
true_total += both_names.count("r")
true_total += both_names.count("u")
true_total += both_names.count("e")

love_total += both_names.count("l")
love_total += both_names.count("o")
love_total += both_names.count("v")
love_total += both_names.count("e")

love_score = str(true_total) + str(love_total)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
