height = input("What is your height: ")
weight = input("What is your weight: ")

bmi_index = int(weight) / (float(height) ** 2)

print("Your BMI index is " + str(bmi_index))
