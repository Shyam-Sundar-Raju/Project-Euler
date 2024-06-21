from math import factorial
flis=[]          #fac of 0 to 9
for i in range(10):
    flis.append(factorial(i))
print(flis)
sum=0            #final sum
for j in range(10,7*factorial(9)):  #upper limit is 7*fac(9) as 8*fac(9) is still a 7 digit number
    fsum=0       #sum of factorials
    for num in str(j):
        fsum+=flis[int(num)] #using flis to speed up process instead of calculating fac each time
    if fsum==j:     #comparing sum of fac and number
        sum+=j
print(sum)