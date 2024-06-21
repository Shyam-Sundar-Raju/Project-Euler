from primePy import primes
max=0                     #maximum sum
mcount=0                  #maximum count
for i in range(3,10000):  #stat value of consecutive primes
    if primes.check(i):   #checking start is prime
        sum=0
        count=0
        num=int(i)
        while sum<1000000:
            if primes.check(num):   #checking if num is prime and updates sum and count
                sum+=num
                count+=1
            if sum>=1000000:       #at the end sum exceeds 1mil, so to remove the last added prime number
                sum-=num
                break
            num+=2
        if mcount<count and primes.check(sum):      #checks and updates max sum and max count
            max=sum
            mcount=count
            print(sum)
    