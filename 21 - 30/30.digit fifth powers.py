sum=0                      #sum of digits that can be written as the sum of 5th powers of their digits 
for i in range (10,10**6):  #10**6 is upper limit as 9**5 mul with 6 gives a 6 digit num and mul with 7 doesn't
    s=0
    for x in str(i):        #iterating through the str of x and finding x**5
        s+=(int(x)**5)
    if s==i:
        sum+=s
print(sum)