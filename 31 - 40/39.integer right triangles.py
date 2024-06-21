mp=0             #maximum perimeter
msol=0           #max solution
for i in range(5,1001):    #i is the perimeter
    lis=[]            #list of solution
    for a in range(1,i//2+1):    #value of a
        for b in range(1,i//2+1): #value of b
            if a**2+b**2==(i-a-b)**2:  #a^2+b^2=c^2
                pyt=[a,b,i-a-b]
                if pyt not in lis:  #appending unique solution
                    lis.append(pyt)
    if len(lis)>msol:    #checking max solution
        msol=len(lis)
        mp=i
print(mp,msol)