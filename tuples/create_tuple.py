# Methods for creating tuples

#-------------------------------------------------------------

# II) taking tuple of integers as input

# A) Tuple Comprehension
b = (int(i) for i in input().split())

# B) Using map function
c = tuple(map(int,input().split()))

#-------------------------------------------------------------

# III) taking tuple of floats as input

# A) Tuple Comprehension
d = (float(i) for i in input().split())

# B) Using map function
e = tuple(map(float,input().split()))

#-------------------------------------------------------------
