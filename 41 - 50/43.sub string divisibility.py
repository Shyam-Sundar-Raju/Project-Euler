from itertools import permutations
l=list(permutations(range(10)))
pl=[2,3,5,7,11,13,17]      #for checking divisibility
sum=0         #final sum
for num in l:
    snum=""
    for j in num:
        snum+=str(j)    #converting list to string of num
    if snum[0]!="0" and int(snum[3])%2==0 and int(snum[5])%5==0:    #first digit cant be zero
        count=0
        for i in range(1,8):
            if int(snum[i:i+3])%pl[i-1]!=0:     #taking 3 digit at a time and checking divisibility
                count+=1
        if count==0:
            sum+=int(snum)  #if passes the test added to sum
print(sum)