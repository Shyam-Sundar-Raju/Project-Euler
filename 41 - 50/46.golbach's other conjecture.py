from primePy import primes
from math import *
num=3       #initializing number
lis=[]      #list of prime numbers less than num
while True:
    if primes.check(num)==False:  #if composite
        count=0          #break statement
        for i in lis:    #checks with each prime number
            x=int(sqrt((num-i)/2))     #checking whether condition is satisfied or not
            if x*x==int((num-i)/2):
                count+=1       #if satisfied next number is checked
                break
        if count==0:           #if not satisfied it is printed
            print(num)
            break
    else:
        lis.append(num)
    num+=2