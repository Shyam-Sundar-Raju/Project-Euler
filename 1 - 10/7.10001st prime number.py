from primePy import primes
n=0                            #num of prime 1 to 10000
x=1                            #num to be checked as prime
while n<10001:
    if primes.check(x):        #checks if prime
        print(n,x)
        n+=1
    x+=1
