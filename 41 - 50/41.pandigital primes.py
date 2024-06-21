from primePy import primes
for i in range(7654321,1,-2):   #only 7 digit num is possible because 987654321 and 87654321 are divisible by 3
    if primes.check(i):
        count=0    #break condition if num not pandigital or 0 is present
        num=str(i)
        y=[a for a in range(1,len(num)+1)]   #for checking if num is pandigital
        for x in num:
            if num.count(x)!=1 or x=="0" or int(x) not in y :  #if digit repeats or 0 or exceeds the number limit for pangigital count is updated
                count+=1
        if count==0:  #count=0 means it is pangigital and prime
            print(i)
            break