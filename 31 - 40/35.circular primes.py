from primePy import primes
lis=[2,5]       #initialize with 2,5 because in line5 2,5 will also be removed
for i in range(3,1000000,2):
    x=str(i)
    if "2" in x or "4" in x or "6" in x or "8" in x or "0" in x or "5" in x:   #no even num or 5 because while rotating num will come to end atleast once
        continue
    elif primes.check(i):     #checking if prime
        lis.append(i)
flis=list(lis)    #duplicate list
for num in lis:
    snum=str(num)
    for _ in range (len(snum)):
        snum=snum[1:]+snum[0]     #rotating first num to last
        if primes.check(int(snum))==False:    #checks if prime for the new num
            if num in flis:
                flis.remove(num)
print(len(flis))