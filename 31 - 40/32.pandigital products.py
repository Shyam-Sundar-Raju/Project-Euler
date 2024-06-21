from itertools import permutations
l = list(permutations(range(1, 10)))  #gives all permutation as a list of tuples
plis=[]          #list of uniqque product
for per in l:    #per will be a tuple
    x=int(str(per[0])+str(per[1]))    #2 digit multiplicand
    y=int(str(per[2])+str(per[3])+str(per[4]))  #3 digit multiplier
    z=int(str(per[5])+str(per[6])+str(per[7])+str(per[8]))  #product can only be a 4 digit num
    a=int(str(per[0]))  #1 digit multiplicand
    b=int(str(per[1])+str(per[2])+str(per[3])+str(per[4])) #4 digit multiplier
    if z not in plis:     #checking if product is unique
        if x*y==z or a*b==z:
            plis.append(z)
print(sum(plis))