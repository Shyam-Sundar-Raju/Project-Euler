from math import *
def pentsol(num):             #function to check if a num is pentagonal or not
    sol=int((1+sqrt(1+24*num))/6)
    if num==sol*(3*sol-1)/2:
        return True
    else:
        return False
lis=[]
for i in range(1,3000): #finding first 3000 pent num , 3000 is just a rough guess
    x=i*(3*i-1)/2
    lis.append(x)
min=1000000000       #just a random value for miminimum of j-k
for j in lis:
    for k in lis:    #taking 2 element at a time and checking j+k and j-k
        p=j+k
        m=abs(j-k)
        if m==0:
            continue
        if pentsol(p) and pentsol(m) and m<min:    #updating minimum value of j-k
            min=m
print(min)