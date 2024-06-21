long=0
vallong=0
lis=[x for x in range(1,1000)]
for two in range(9):               #removing all numbers which can be written in the form 2^a x 5^b as they have finite decimal
    for five in range(5):
        num=(2**two)*(5**five)
        if num in lis:
            lis.remove(num)
for i in lis:                   #converting all remaining numbers to lowest form without any 2 or 5 as 2,5 can give numbers before repeating part, like 0.533333333
    ind=lis.index(i)
    while i%2==0:
        i/=2
    while i%5==0:
        i/=5
    lis[ind]=int(i)
mcount=1         #it is the max period of repetition
mval=0
for j in lis:
    count=1      #period of repetition
    while True:
        if (10**count-1)%j==0:     #the period of 1/n is equal to the smallest integer x>=1, such that 10^x-1 is divisible by n. for this to work n shoudn't have any divisor as 2,5
            break
        else:
            count+=1
    if mcount<count:
        mcount=count
        mval=j
print(mval)