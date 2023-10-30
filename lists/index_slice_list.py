# indexing and slicing
from lists import list_var1

list1 = list_var1([11,22,33],[23,34,45],[45,67,89])
list1.display()

a = list1.a
b = list1.b
c = list1.c

#indexing
for i in range(len(a)):
    print(f"{i}th element of a is {a[i]}")
    print(f"{i}th element of b is {b[i]}")
    print(f"{i}th element of c is {c[i]}")
    print()

#slicing
for i in range(len(a)):
    for j in range(len(a)):
        print(f"The elements between {i}th index and {j}th index of a are : {a[i:j+1]}")
        print(f"The elements between {i}th index and {j}th index of b are : {b[i:j+1]}")
        print(f"The elements between {i}th index and {j}th index of c are : {c[i:j+1]}")
        print()