count=2   #series number
num=0       #num of digits
x,y=1,1
while num!=1000:
    x,y=y,x+y     #updating the series
    num=len(str(y))   #length of last num in series
    count+=1
print(count)