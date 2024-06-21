num1=10            #start value
while True:
    count=0       #for break statement
    num2, num3, num4, num5, num6 = num1*2, num1*3, num1*4, num1*5, num1*6          #the 6 numbers
    s1, s2, s3, s4, s5, s6 = str(num1), str(num2), str(num3), str(num4), str(num5), str(num6)   #string of 6 numbers
    if len(s1)==len(s2)==len(s3)==len(s4)==len(s5)==len(s6):                   #if length of each string is same
        l1,l2,l3,l4,l5,l6=list(s1),list(s2),list(s3),list(s4),list(s5),list(s6)    #list of 6 numbers
        for i in l1:      #checking if all numbers in num1 is present in all other 5 numbers
            if i not in l2 or i not in l3 or i not in l4 or i not in l5 or i not in l6:
                count+=1         #breaks the loop
                break
        if count==0:        #this means all number in num1 is present in all other 6 as well
            print(num1)
            break
    num1+=1