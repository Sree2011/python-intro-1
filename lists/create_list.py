# Methods for creating lists

# I) taking list of strings as input
a = input().split()

#-------------------------------------------------------------

# II) taking list of integers as input

# A) List Comprehension
b = [int(i) for i in input().split()]

# B) Using map function
c = list(map(int,input().split()))

#-------------------------------------------------------------

# III) taking list of floats as input

# A) List Comprehension
d = [float(i) for i in input().split()]

# B) Using map function
e = list(map(float,input().split()))

#-------------------------------------------------------------


# IV) taking multiple integer variables as input

# A) List Comprehension
f,g= [int(i) for i in input().split()]

# B) Using map function
h,i = list(map(int,input().split()))

#-------------------------------------------------------------


# V) taking multiple float variables as input

# A) List Comprehension
j,k = [float(i) for i in input().split()]

# B) Using map function
l,m= list(map(float,input().split()))

#-------------------------------------------------------------


# VI) taking multiple string variables as input

# A) List Comprehension
n,o= [i for i in input().split()]

# B) Using map function
p,q = list(map(str,input().split()))


#-------------------------------------------------------------



