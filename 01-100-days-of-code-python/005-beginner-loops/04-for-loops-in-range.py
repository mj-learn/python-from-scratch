# Range is 0 to 9
for number in range(10):
    print(number)

print()

# Range is from 3 to 9
for number in range(3, 10):
    print(number)

print()

# Range is 2, 4, 6, 8
for number in range(2, 10, 2):
    print(number)

print()

# Total sum between 1 and 100
total = 0
for number in range(1, 101):
    total += number

print(f"Total sum between 1 and 100 is {total}")
