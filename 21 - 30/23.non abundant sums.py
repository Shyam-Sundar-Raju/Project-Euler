import math
abnum=[]
for i in range(12,28112):          #finds all abundant number below 288112 as 12 is the smallest ab num and 28123-12=28111
    sum=1
    for j in range(2,int(math.sqrt(i)+1)):     #sum of divisors of the number
        if i%j==0:
            sum+=j
            if i/j!=j:
                sum+=i/j
    if sum>i:              #checking if it is ab num
        abnum.append(i)
lis=[x for x in range(1,28123)]
nlis=[]
for a in abnum:         #finding numbers which are sum of two ab num using abnum lis
    for b in abnum:
        ab=a+b
        if ab<28123:       #appending if num is less than 28123
            nlis.append(ab)
        elif ab>28122:
            break
nlis=set(nlis)       #this helps remove all duplicate elements
nlis=list(nlis)
ite=0
while ite<len(lis):     #removing all the num which are sum of ab num from lis with the help of nlis
    if lis[ite] in nlis:
        lis.pop(ite)
    else:
        ite+=1
sum=0
for z in lis:       #adding to find total sum
    sum+=int(z)
print(sum)