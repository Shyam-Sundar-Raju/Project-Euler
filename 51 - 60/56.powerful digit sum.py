msum=0       #maximum sum of digits
for i in range(90,100):     #bigger numbers have more digits leading to max sum
    for j in range(90,100):   #bigger power gives more digits leading to max sum
        sum=0
        num=str(i**j)
        for x in num:   #finding sum of digits
            sum+=int(x)
        if sum>msum:
            msum=sum
print(msum)