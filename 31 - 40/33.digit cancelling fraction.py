from fractions import Fraction
lis=[]                   #list of fraction in form of nested list
for i in range(11,100):
    for j in range(11,100):
        if i<j:          #fraction value is less than 1
            if "0" not in str(i) and "0" not in str(j):   #this is to eleminate x/0 form and trivial solution like 10/50 or 40/90
                fac=Fraction(i,j)        #fractional form of i,j
                w=int(str(i)[0])         #seperate digits of i,j used for comparision
                x=int(str(i)[1])
                y=int(str(j)[0])
                z=int(str(j)[1])
                if (w==z and x!=y):      #checking for only one common number
                    if fac==Fraction(x,y):
                        lis.append([x,y])
                elif (w!=z and x==y):
                    if fac==Fraction(w,z):
                        lis.append([w,z])
                elif (w==y and x!=z):
                    if fac==Fraction(x,z):
                        lis.append([x,z])
                elif (w!=y and x==z):
                    if fac==Fraction(w,y):
                        lis.append([w,y])
nu=1              #numerator
de=1              #denominator
for a in lis:
    nu*=a[0]
    de*=a[1]
print(Fraction(nu,de))   #gives product of those fraction in simplefied form