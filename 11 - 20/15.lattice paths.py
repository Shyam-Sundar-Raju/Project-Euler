import math
"""let's consider that a ant is moving in the lattice,
then it can only move 20 times right and 20 times down
so we should arrange the 40 direction in a permutation"""
x=math.factorial(40)
x/=(math.factorial(20)**2)
print(x)
"""as there is 2 20 objects identical we divide yhe x with 20!*20!
to get the answer.
this is now complete , hence the total permutation is calculated
and the identical element permutation cases is removed"""
