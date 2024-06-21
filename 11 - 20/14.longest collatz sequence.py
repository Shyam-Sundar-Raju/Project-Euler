mcount=[0,0]
for num1 in range(1,1000000):
    num=num1                 #just to print the num in print statment
    count=0                  #num of changes
    while True:
        if num1==1:
            count+=1
            break
        elif num1%2==0:
            count+=1
            num1/=2
        else:
            count+=1
            num1=(num1*3)+1
    if count>mcount[0]:       #checks max count and updates
        mcount[0]=count
        mcount[1]=num
        print(mcount)
input("hi")
