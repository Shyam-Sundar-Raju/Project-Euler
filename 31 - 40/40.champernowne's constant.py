length=0    #length of string
s=""        #string of the decimal part
x=1         #number to be added to s
while length<1000001:
    s+=str(x)   #appending x to s
    x+=1        #incrementing x
    length=len(s)   #updating len of s
d1=int(s[0])
d10=int(s[9])        #accessing the elements required
d100=int(s[99])
d1000=int(s[999])
d10000=int(s[9999])
d100000=int(s[99999])
d1000000=int(s[999999])
print(d1*d10*d100*d1000*d10000*d100000*d1000000)