from sympy import primefactors
def primefac(l):       #this function creates the list of prime factors for the given num 
    f=primefactors(l)
    nl=[]
    for i in f:
        count=0
        while l%i==0:
            count+=1
            l/=i
        nl.append(i**count)
    return nl
n1,n2,n3,n4=644,645,646,647   #start case as given in question
f1=primefac(n1)
f2=primefac(n2)    #finding prime fac for the numbers
f3=primefac(n3)
f4=primefac(n4)
while True:
    if len(f1)!=4 or len(f2)!=4 or len(f3)!=4 or len(f4)!=4:  #checking for 4 prime fac and if not present updating n and f
        n1,n2,n3,n4=n2,n3,n4,n4+1
        f1,f2,f3,f4=f2,f3,f4,primefac(n4)
        continue
    flis=f1+f2+f3+f4
    for j in flis:       #checking if distinct prime factors
        if flis.count(j)!=1:
            break
    else:
        print(n1,n2,n3,n4)  #if distinct prime fac print and break
        break
    n1,n2,n3,n4=n2,n3,n4,n4+1        #updating n and f
    f1,f2,f3,f4=f2,f3,f4,primefac(n4)