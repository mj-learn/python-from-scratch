# Morphy's law which states that anything that can go wrong probably will, eventually at some point, go wrong.

try:
    # Something that might cause an exception
    pass
except IndexError:
    # Handling single error
    pass
except FileNotFoundError as error_message:
    # Handling single error with reference
    print(f"FileNotFoundError: {error_message}")
except (ValueError, KeyError, TypeError):
    # Handling more than one error with single except
    pass
except:
    # Too broad exception
    # PEP 8: E722 do not use bare 'except'
    # Broad (Default) exception must be at last
    pass
else:
    # Do this if there were no exceptions
    pass
finally:
    # Do this no matter what happens
    pass

try:
    # FileNotFound
    # with open("not_exist.txt", "r") as file:
    #     file.read()

    # KeyError
    # a_dictionary = {"key": "value"}
    # value = a_dictionary["non_existent_key"]

    # IndexError
    # fruit_list = ["Apple", "Banana", "Pear"]
    # fruit = fruit_list[3]

    # TypeError
    # text = "abc"
    # print(text + 5)

    name = "Angela"

except FileNotFoundError:
    # Do this if there was an FileNotFoundError
    print("File missing")

except KeyError as error_msg:
    # Do this if there was an KeyError
    print(f"That key {error_msg} does not exist.")

else:
    # Do this if there were no exceptions
    print(name)

finally:
    # Do this no matter what happens
    print("End of try catch block")
