import json

dict_data = {
    "John": {
        "age": 30,
        "city": "New York",
    }
}

# Serialize
# Serialization is the process of converting an object or data structure into a format that can be easily
# stored, transferred, or communicated between different systems. The serialized format is often a sequence of bytes
# or a text format like JSON or XML.
json_data = json.dumps(dict_data)  # Serialize to JSON format

print(f"{type(json_data)}")  # Output: <class 'str'>

# Deserialize
# Deserialization is the reverse process—converting a sequence of bytes or a text format back into its original data
# structure or object. This allows you to restore the object to its original form after it has been serialized.
new_data_dict = json.loads(json_data)  # Deserialize from JSON format

print(new_data_dict)  # Output: {'John': {'age': 30, 'city': 'New York'}} --> same as dict_data

# Write (save) json data to a file
with open("data.json", "w") as data_file:
    json.dump(dict_data, data_file, indent=4)  # Serialize to JSON and write to file

# Read json data from a file
with open("data.json", "r") as data_file:
    data = json.load(data_file)  # Deserialize from JSON format and return it

print(
    f"{type(data) = } --> {data}"
)  # Output: type(data) = <class 'dict'> --> {'John': {'age': 30, 'city': 'New York'}}

dict_data_2 = {
    "Guido": {
        "age": 68,
        "city": "Amsterdam",
    }
}

# UPDATE JSON FILE -------------------------------------------

# 1 - Reading old json data
with open("data.json", "r") as data_file:
    data_2 = json.load(data_file)  # Deserialize from JSON format and return it (Same as data from above)

# 2 - Updating deserialized old data
data_2.update(dict_data_2)  # Basic dict to dict update

# 3 - Write (save) updated data
with open("data.json", "w") as data_file:
    json.dump(data_2, data_file, indent=4)  # Serialize to JSON and write to file
