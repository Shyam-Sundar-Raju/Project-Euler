from primePy import primes
sum=5                        #for 2 and 3
for i in range(5,2000000,6): #all prime numbers except 2,3 are in the form 6x+-1
    if primes.check(i):
        sum+=i               #if prime add to sum
for j in range(7,2000000,6):
    if primes.check(j):
        sum+=j
print(sum)