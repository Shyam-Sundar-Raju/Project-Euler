from primePy import primes
from itertools import permutations
for i in range(1000,3340):        #the upper limit is 3339 becaue 3339+6660=9999
    if primes.check(i) and primes.check(i+3330) and primes.check(i+6660):      #checking if the 3 numbers are prime
        l = list(permutations(list(str(i))))           #creating a list of permutation of 4 numbers
        if tuple(str(i+3330)) in l and tuple(str(i+6660)) in l:     #checking if the other 2 numbers are in the permutation
            print(i,i+3330,i+6660)