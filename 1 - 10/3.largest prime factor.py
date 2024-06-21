import math

n=600851475143
for i in range(2,int(math.sqrt(n))+1):    #looping till sqrt(n)
    while n%i==0:          #checking divisibility           
        n=n/i              #dividing n/i to reduce the size of number
    print(i)
    if n==1:               #found all prime factors if n==1
        break
