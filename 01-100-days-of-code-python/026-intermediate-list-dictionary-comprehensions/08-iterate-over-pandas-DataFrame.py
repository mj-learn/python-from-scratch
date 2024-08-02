import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Looping through dictionaries
for key, value in student_dict.items():
    print(f"{key = }")
    print(f"{value = }")

print()

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print()

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # print(f"{index = }")
    # print(f"{row}")
    print(f"{row.student}")
