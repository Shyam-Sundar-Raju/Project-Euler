from math import *
count=0            #count of com>1 mil
for n in range(1,101):  #value of n
    for r in range(0,n+1):  #value of r
        if factorial(n)/(factorial(r)*factorial(n-r))>1000000:   #checking if nCr>1 mil
            count+=1
print(count)