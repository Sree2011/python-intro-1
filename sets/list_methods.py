from sets import set_var1

set1 = set_var1({11,22,33},{22,33,44},{33,44,55})

a,b,c = set1.a,set1.b,set1.c

# Note, A,B and C are Sets

# Adds an element to the set
print("Before adding = ",a)
a.add(12)
print("After adding = ",a)
print()

# Removes all the elements from the set
test_set = {11,88,66,55,33}
print("Before clearing = ",test_set)
test_set.clear()
print("After clearing = ",test_set)
print()

# Returns a copy of the set
g = a.copy()
print("A = ",a)
print("G = " ,g)
print()

# Diff = A - B
print("The set difference between a and b is ",a.difference(b))
print()

# Diff_Update = A - (A intersection B)
a.difference_update(b)
print("The elements present only in a are: ",a)
print()

# Remove a specified item
test_set = {11,88,66,55,33}
print("Before removing = ",test_set)
test_set.discard(55)
test_set.remove(33)
print("After removing = ",test_set)
print()

# A intersection B
print(f"The intersection of {c} and {b} is {c.intersection(b)}")

# Intersection_Update = (A intersection B ) - A
b.intersection_update(c)
print(f"The elements present common in B and C are: {b}")
print()

# if(len(A intersection B) == 0):
#   return True
# else:
#     return False

print("Does B and C have an intersection? --> ",b.isdisjoint(c))
print()

# Check if A is Sub Set of B
print("Is C a subset of B? --> ",b.issubset(c))
print()

# Check if A is Super Set of B
print("Is B a superset of C? --> ",c.issuperset(b))
print()

# Pop the first element
c.pop()
print("C after pop: ",c)
print()
# Symmetric Difference of A and B
print(f"Symmetric Difference of {b} and {c} is {b.symmetric_difference(c)}")
print()

# Symmetric Difference Update of A and B
a.symmetric_difference_update(c)
print(f"Updated Symmetric Difference of {a} and {c} is {a}")
print()

# A Union B
print(f"The Union of {b} and {c} is {b.union(c)}")

# Add a list to set
a.update([112,33,987])
print(a)