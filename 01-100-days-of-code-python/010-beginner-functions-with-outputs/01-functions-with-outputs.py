# Simple function
def simple_function():
    print("Hello")


# Function with inputs
def function_with_input(parameter):
    print(parameter)


# Function with outputs (return)
def function_with_output(num):
    result = num + 3
    return result


# Functions with multiple return values
# After the first triggered return we exit from function
def function_with_many_returns(rating):
    if rating > 8:
        return "This girl is on fire"

    if rating > 4:
        return "She's a solid 5 out of 10, but with her sense of humor, she could make a funeral feel like a wild bachelor party!"

    if rating > 0:
        return "She's a 1 out of 10, but her personality is so magnetic that even her reflection doesn't want to leave!"


# Exercise
def format_name(first_name, last_name):
    # return f"{first_name} {last_name}".title()
    return (first_name + " " + last_name).title()  # hah this work :D love python


# print(format_name("mOn", "jofn")) # work but exercise is to assign to variable

name = format_name("mOn", "jofn")
print(name)
