mnum=0             #maximum concated product
for i in range(10000):  #upper limit is 10000 as 10000 has 5 digit for itself
    s="0"      #string of num having concated product
    b=0        #setting break value
    for j in range(1,10):  #upper limit for multiplication is 9 because 10 will give 10 gigit even for 1
        x=str(i*j)
        for y in x:
            if y!="0" and y not in s:  #looping through each num in product and checking if present in s
                s+=y
            else:    #if 0 or repeated num breaks the loops
                b+=1
            if b!=0:
                break
        if b!=0:
            break
    if mnum<int(s):     #checking and updating mnum
        mnum=int(s)
print(mnum)
                