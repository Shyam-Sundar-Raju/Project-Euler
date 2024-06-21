from primePy import primes
count=0
num=11    #initialization for num
sum=0     #final sum
while count<11:  #runs 11 times
    x=str(num)
    if "0" in x or "4" in x or "6" in x or "8" in x or x[0] in ["1","9",] or x[-1] in ["1","9"] or primes.check(num)==False:   #0,4,6,8 cant be in num and 1,9 cant come in start or end
        num+=2   #skipping even numbers
    else:
        if primes.check(num):
            true=0            #value for finding truc=ncatable prime
            a=int(num)
            for i in range (len(x)-1):   #checking by removing last num
                if primes.check(a)==False:
                    true+=1
                a=int(str(a)[:-1])     #removing last num
            b=int(num)
            for i in range (len(x)-1):   ##checking by removing first num
                if primes.check(b)==False:
                    true+=1
                b=int(str(b)[1:])      ##removing first num
            if true==0:     #checking if truncate prime
                sum+=num
                count+=1      #updating count
                print(num)
        num+=2                   #updating num to check
print(sum)