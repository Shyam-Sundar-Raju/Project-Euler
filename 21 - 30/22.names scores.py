nfile=open("22.names.txt","r")      #opening text file
r=nfile.readline()
nlis=r.split(",")                   #converting into list
flis=[]
for i in nlis:
    flis.append(i[1:-1])            #removing the extra "" present
flis.sort()
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #giving value to alphabets
namescore=0                         #final ans
mul=1                               #multiplying factor which is incremented each time
for name in flis:
    for alph in name:
        namescore+=(mul*((alpha.index(alph)+1)))
    mul+=1
print(namescore)
