lis=[]                #list of powers
for i in range(2,101):
    for j in range(2,101):
        x=i**j
        if x not in lis:   #if not present in list then appends
            lis.append(x)
print(len(lis))