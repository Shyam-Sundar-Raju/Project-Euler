from primePy import primes
mcount=0                 #max count of consecutive primes
mab=0                    #value of a*b
for b in range(1001):    #b cant be -ve and b should be prime, because while n=0 x=b
    if primes.check(b):
        for a in range(-999,1000):
            count=0       #count of consecutive primes
            n=0           #value of n in equation
            while True:
                x=(n**2)+(a*n)+b   #substituting values in equation
                if x>=0 and primes.check(x):
                    count+=1
                else:
                    break
                n+=1
            if mcount<count:    #checking and updating mab wrt mcount
                mcount=count
                mab=a*b
print(mab)