import math
tsum=0                                            #sum of all amicable num under 10000
lis=[x for x in range(1,10001)]
dlis=[1,]                                          #sum of divisor list of 10000 num
for num in lis[1:]:
    dsum=1                                        #sum of divisor of a num
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            dsum+=i
            dsum+=(num/i)
    dlis.append(dsum)
for a in lis:
    if a in dlis:                                 #checking a=db
        dbInd=dlis.index(a)                       #finding index of db
        b=lis[dbInd]                              #finding b
        daInd=lis.index(a)                        #finding index od da
        da=dlis[daInd]                            #finding da
        if b==da and a!=b:                        #a=db and b=da and a!=b
            tsum+=(a+b)
            lis.remove(a)                       #removing a,b,da,db form lists
            lis.remove(b)
            dlis.remove(da)
            dlis.remove(a)
            print(a,b)
print(tsum)                                     #/2 because same pair repeats twice
