names = ["Guido", "Angela", "Mitnick"]

# new_dict = {new_key:new_value for item in list}
names_and_len_dict = {person: len(person) for person in names}
print(names_and_len_dict)  # Output: {"Guido": 5, "Angela": 6, "Mitnick": 7}

# new_dict = {new_key:new_value for item in list if test}
names_and_len_dict_2 = {person: len(person) for person in names if len(person) > 5}
print(names_and_len_dict_2)  # Output: {"Angela": 6, "Mitnick": 7}

# new_dict = {new_key:new_value for key,value in dict.items()}
new_names_and_len_dict = {name.upper(): len for name, len in names_and_len_dict.items()}
print(new_names_and_len_dict)  # Output: {"GUIDO": 5, "ANGELA": 6, "MITNICK": 7}

# new_dict = {new_key:new_value for key,value in dict.items() if test}
new_names_and_len_dict_2 = {name.upper(): len for name, len in names_and_len_dict.items() if len > 5}
print(new_names_and_len_dict_2)  # Output: {ANGELA": 6, "MITNICK": 7}
