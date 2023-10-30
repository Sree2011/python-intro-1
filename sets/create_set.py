# Create set using set() method

g = set()

h = {}

print("Type of g = ",type(g))
print("Type of h = ",type(h))



# II) taking set of integers as input

# A) Set Comprehension
b = {int(i) for i in input().split()}
print(type(b))

# B) Using map function
c = set(map(int,input().split()))
print(type(c))
#-------------------------------------------------------------

# III) taking set of floats as input

# A) Set Comprehension
d = {float(i) for i in input().split()}

# B) Using map function
e = set(map(float,input().split()))

#-------------------------------------------------------------
