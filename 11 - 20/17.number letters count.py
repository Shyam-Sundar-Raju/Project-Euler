from num2words import num2words
sum=0             #final sum
for i in range(1,1001):
    num=num2words(i)   #gives the word for number entered 
    for j in num:
        if j==" " or j=="-":   #removing space and hyphen if any
            continue
        else:
            sum+=1
print(sum)