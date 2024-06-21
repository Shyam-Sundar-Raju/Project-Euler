f=open("67.triangle.txt","r")
lis=f.readlines()
flis=[]
for i in lis:
    flis.append(i[:-1].split())
lis1=[]
for j in flis:
    l=[]
    for k in j:
        l.append(int(k))
    lis1.append(l)
for rind in range(len(lis1)-2,-1,-1):     #takes one row at a time from the bottom and adds the bigger of 2 number to the upper row number
    for cind in range(rind+1):   #the number is added to the bigger number of the 2 numbers below it.
        lis1[rind][cind]+=max(lis1[rind+1][cind],lis1[rind+1][cind+1])
print(lis1[0])        #by this method at last the top number will be the max path sum