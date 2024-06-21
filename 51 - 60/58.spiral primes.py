from primePy import primes
from math import *
nu=3         #number of prime in diagonal
de=5         #count of numbers in diagonal
skip=4       #already considered number spiral till 9, so starting skip value with 4
num=9
while nu/de>=0.1:
    for _ in range(4):
        num+=skip     #updating the num with skip
        if primes.check(num):   #checking if num is prime and updating nu
            nu+=1
    de+=4
    skip+=2   #updating skip value
print(sqrt(num))  #sqrt of num will give the side length