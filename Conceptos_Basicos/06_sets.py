### Sets ###
my_set = set()
my_other_set = {}

my_set = {1, 2, 3}

print(type(my_set))  # <class 'set'>
print(type(my_other_set))  # <class 'dict'>
# Sets are unordered collections of unique elements

my_other_set = {"juan", "pepe", "maria"}
print(my_other_set)  # {'pepe', 'maria', 'juan'}
print(type(my_other_set))  # <class 'set'>

print(len(my_other_set))  # 3
print("pepe" in my_other_set)  # True
print("pepe" not in my_other_set)  # False
print("pepe" in my_other_set)  # True

my_other_set.add("pepe")  # No error, but no change
my_other_set.add("luis")
print(my_other_set)  # {'pepe', 'maria', 'juan', 'luis'}
my_other_set.remove("pepe")
print(my_other_set)  # {'maria', 'juan', 'luis'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)  # {'maria', 'juan', 'luis'}
