count=0       #final count
for ite in range(1000,0,-1):    #for 1000 expansions
    nu=1         #start numerator
    de=2         #start denominator
    for i in range(ite-1):     #the fraction is added to 2 and inversed for ite-1 times (this can be observed in the question)
        nu=de*2+nu
        nu,de=de,nu
    nu=de*1+nu        #finally it is added to 1 to get the final numerator
    if len(str(nu))>len(str(de)):    #checking for condition
        count+=1
print(count)