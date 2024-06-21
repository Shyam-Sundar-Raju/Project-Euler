from math import *
n=40755           #first number to be t,p,h and all h are t
start=int((1+sqrt(4+4*2*n))/4)   #finding the value of n
while True:
    start+=1           #increasing n and checking if h=p
    hnum=start*(start*2-1)    #gives next h after 40755
    psol=int((1+sqrt(1+24*hnum))/6)   #finds a value for p using hnum
    pnum=psol*(3*psol-1)/2    #calculates a p with before found psol
    if hnum==pnum:          #if both are equal , that is the answer
        print(hnum)
        break