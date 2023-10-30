from tuples import tuple_var1

tuple1 = tuple_var1((11,22,33),(44,55,66),(77,99,54))

a = tuple1.a
b = tuple1.b
c = tuple1.c

#counting no.of occurences of a element in a tuple

print("The count of 77 in c is ",c.count(77))
print("The count of 99 in c is ",c.count(99))
print()

# Finding index of an element in the tuple
print("The index of 66 in b is ",b.index(66))
print()

#finding minimum and maximum elements in a tuple
print("Minimum element of c is ",min(c))
print("Maximum element of c is ",max(c))
print()

#finding the sum of elements
print("Sum of elements of c is ",sum(c))
print()

# Reversing a tuple using slicing technique
# New tuple is created
print("Before reversing = ",a)
d = a[-1::-1]
print("After reversing = ",d)
print()

#clearing a tuple

test_tup = (11,22,33,45)
print("Before clearing = ",test_tup)
test_tup = tuple()
print("After clearing = ",test_tup)
print()

#concatenating two tuples

print("Before concatenating = ",a,"\n",b)
print("After concatenating = ",(a+b))
