#### Dictionaries ####

my_dict = dict()  # Creating an empty dictionary
my_dict = {}
print(type(my_dict))  # Another way to create an empty dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
print(my_dict["name"])  # Accessing a value by key
print(my_dict.get("age"))  # Another way to access a value by key
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs
print(my_dict["age"] + 5)  # Accessing a value and performing an operation

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"],
    "is_student": False,
    "lenguajes": {"Python", "Java", "C++"},
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
    },
}
print(my_dict)
print(type(my_dict))
print(my_dict["hobbies"])  # Accessing a list within a dictionary
print(len(my_dict))  # Length of the dictionary
