# creates three lists of 50 random numbers from 1 to 250
import random
a_list = []
for i in range(0,50):
    n = random.randint(1,250)
    a_list.append(n)
b_list = []
for i in range(0,50):
    n = random.randint(1,250)
    b_list.append(n)
c_list = []
for i in range(0,50):
    n = random.randint(1,250)
    c_list.append(n)
    
# convert the lists to sets
a_set = set(a_list)
b_set = set(b_list)
c_set = set(c_list)

# creates a union for a_set and b_set
ab_union = a_set | b_set

# creates intersect for b_set and c_set
bc_intersect = b_set & c_set

# smallest appropriate universe for these sets
Universe = set(range(1,251))

# returns the complement of a given set
def comp(s):
    return Universe - s
# find complement of a_set  
a_comp = comp(a_set)
# prove a_comp really is the complement of a_set
# the intersect holds common values between two sets, so if the intersect is empty, a_comp really is the complement of a_set
a_intersect = a_set & a_comp
print(a_intersect)

# associativity of the operations union and intersection can be verified
leftside = a_set | (b_set & c_set)
rightside = (a_set | b_set) & (a_set | c_set)
print(leftside == rightside)
