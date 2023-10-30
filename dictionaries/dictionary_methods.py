from dictionaries import dict_var1

dict1 = dict_var1({'Name': 'Sai','Branch': 'EEE','Roll No':66},
                  {'Name': 'Sree','Branch': 'ECE','Roll No':69},
                  {'Name': 'Nandini','Branch': 'EIE','Roll No':76})

a = dict1.a
b = dict1.b
c = dict1.c

# Clear all the elements in a dictionary
test_dict = {'Name': 'Sai','Branch': 'EEE','Roll No':66}
print("Before clearing = ",test_dict)
test_dict.clear()
print("After clearing = ",test_dict)
print()

# Copy all the elements
d = a.copy()
print("Original dictionary = ",a)
print("Copied dictionary = ",d)
print()

# Return specified keys and values
print("The specified keys and values = ",dict.fromkeys(["Name","Class","Section"],"A magic horse"))
print()

# Retrieve value based on key
print("The value of Name in a is ",a.get("Name"))
print()

# The key value pairs in dict
print("The key - value pairs in b are = ",b.items())
print()

# The keys in dict
print("The keys in b are = ",b.keys())
print()

# The values in dict
print("The values in b are = ",b.values())
print()

# Removing specified key
print("Before removing = ",c)
c.pop("Roll No")
print("After removing = ",c)
print()

# Removing last inserted key
print("Before removing = ",c)
c.popitem()
print("After removing = ",c)
print()

# Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value
print("Before adding key = ",c)
c.setdefault("Branch","ECE")
print("After adding key = ",c)
print()

# Updates the dictionary with the specified key-value pairs
print("Before adding key = ",c)
c.update({"Roll No":123450})
print("After adding key = ",c)
print()



