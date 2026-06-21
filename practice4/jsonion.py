import json

# Python dictionary (dict)
user_data = {
    "name": "Ivan",
    "age": 21,
    "is_student": True,
    "skills": ["Python", "Git"],
    "courses": None
}

# dumps() - converts a Python object into a JSON string (serialization)
# ensure_ascii=False preserves non-ASCII characters as they are, indent sets indentation for readability
json_string = json.dumps(user_data, ensure_ascii=False, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>


# loads() - converts a JSON string back into a Python object (deserialization)
raw_json = '{"name": "Ivan", "age": 21, "is_student": true, "courses": null}'
parsed_dict = json.loads(raw_json)
print(parsed_dict["name"]) # Accessing data like a regular dictionary -> Ivan
print(type(parsed_dict))   # <class 'dict'>


# dump() - writes a Python object directly to a file in JSON format
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)


# load() - reads JSON data directly from a file and converts it into a Python object
with open("user.json", "r", encoding="utf-8") as file:
    data_from_file = json.load(file)
    print(data_from_file["skills"])  # -> ['Python', 'Git']