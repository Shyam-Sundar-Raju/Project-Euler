sum=0               #final sum
for i in range(1,1000000):
    y=int(i)
    x=str(i)
    if x==x[::-1]:   #checking palindrome for base10
        rem=""
        while y>0:   #converting to binary
            rem+=str(y%2)
            y//=2
        if rem==rem[::-1]:  #checking palindrome for base2
            sum+=i
print(sum)