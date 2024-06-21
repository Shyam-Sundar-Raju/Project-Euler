num1=0
num2=1
s=0
while num2<=4000000:
    num1,num2=num2,num1+num2   #changing values
    if num2%2==0:
        s+=num2
print(s)
