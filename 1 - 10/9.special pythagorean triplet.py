product=0                                 #a2+b2=c2 and a+b+c=1000
for i in range(500,1,-1):           #a ranges form 1 to 500 due to a+b>c and a<c
    for j in range(500,1,-1):       #b ranges from 1 to 500 due to a+b>c and b<c
        if (i**2+j**2)==((1000-i-j)**2):   #c=1000-a-b
            product=i*j*(1000-i-j)         #a*b*c
            print(i,j)
            print(product)
            break
    if product!=0:
        break
