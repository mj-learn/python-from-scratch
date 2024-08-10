# Raising your own Exceptions
# raise TypeError("My type-senses are tingling... and they don't like what they see!")

# When might you want to raise errors?

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)
