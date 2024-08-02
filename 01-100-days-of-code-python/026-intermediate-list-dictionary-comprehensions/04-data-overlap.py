# Instructions
#
# 💪 This exercise is HARD 💪
# Take a look inside 04-file1.txt and 04-file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 2
# 3
# and file2.txt contained:
#
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.
#
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]

with open("04-file1.txt") as file_1:
    data_1 = file_1.readlines()

data_1 = [int(item) for item in data_1]

with open("04-file2.txt") as file_2:
    data_2 = file_2.readlines()

data_2 = [int(item) for item in data_2]

result = [num for num in data_1 if num in data_2]

# Write your code above 👆
print(result)
