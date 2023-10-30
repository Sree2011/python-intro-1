from lists import list_var1

list1 = list_var1([11,22,33],[44,55,66],[77,99,54])

a = list1.a
b = list1.b
c = list1.c

# Append an element to the last of a list
print("Before append = ",a)
a.append(12)
b.append([13,23,45])
print("After append = ",a)
print()


# Sort the list
print("Before sorting = ", a)
a.sort()
print("After sorting = ",a)
print()


# copying the list to another list
# note that the original list is unaffected of the modifications on copied one

d = b.copy()

print("Original list = ",b)
print("Copied list = ",d)
print()
d.append(87)

print("Modified Original list = ",b)
print("Modified Copied list = ",d)
print()

#extending the list
print("Before extending = ",a)
a.extend([13,23,45])
print("After extending = ",a)
print()

#clear all the elements of list
print("Before clearing = ",a)
a.clear()
print("After clearing = ",a)
print()

#reverse the elements of the list
print("Before reversing = ",b)
b.reverse()
print("After reversing = ",b)
print()

#remove an element from the list
print("Before removing = ",c)
c.remove(99)
print("After removing = ",c)
print()

#remove an element from the list by index
print("Before removing = ",c)
c.pop(1)
print("After removing = ",c)
print()

#insert an element to the list
print("Before inserting = ",c)
c.insert(1,99)
c.insert(2,77)
c.insert(3,99)
c.insert(4,77)
print("After inserting = ",c)
print()

#counting no.of occurences of a element in a list

print("The count of 77 in c is ",c.count(77))
print("The count of 99 in c is ",c.count(99))
print()

# Finding index of an element in the list
print("The index of 66 in b is ",b.index(66))
print()

#finding minimum and maximum elements in a list
print("Minimum element of c is ",min(c))
print("Maximum element of c is ",max(c))
print()

#finding the sum of elements
print("Sum of elements of c is ",sum(c))