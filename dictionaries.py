# Dictionaries are helpful for storing data in an organized manner. Each
# element in a dictionary is a key-value pair that are related to each other in
# some way. Any type can be a key or value.

# An example dictionary of people and their age.
a_dict = {"John":18, "Stacy":19, "Kyle":20}


# To access the data in a dictionary, we use the index operators [] with the
# key.

print("Get value from key")
print(a_dict["John"]) # 18.
print(a_dict["Stacy"]) # 19.
print(a_dict["Kyle"]) # 20.
print("\n")


# We can also add to a dictionary like so.
print("Adding to a dictionary")
a_dict["Holly"] = 21
print(a_dict)
print("\n")
