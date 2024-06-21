z=0                              #a number reads same from both side
for i in range(999,99,-1):       #first num
    for j in range (999,99,-1):  #second num
        y=i*j
        x=str(i*j)
        if x==x[::-1] and y>z:   #converted to string and check if palindrome
            z=y                  #if palin then check if largest product
print(z)