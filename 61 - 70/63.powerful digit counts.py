count=0
for base in range(1,10):   #base cant be 10 as 10^exp will always be bigger than exp
    exp=1
    while len(str(base**exp))==exp:   #checking if len=exp, len cant be > exp (by observation) and if len<exp it doesnt satify the condition
        count+=1
        exp+=1
print(count)