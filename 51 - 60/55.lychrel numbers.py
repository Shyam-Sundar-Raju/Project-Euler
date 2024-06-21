count=0       #count of lychrel numbers
for i in range(1,10000):
    si=i
    for _ in range(50):    #trying to finf palindrome for 50 times
        ri=int(str(si)[::-1])  #reversing the number
        si+=ri                #adding with the reversed number
        if str(si)==str(si)[::-1]:     #checking if the result is palindrome
            break
    else:           #if loop ends naturally, then number is lychrel
        count+=1
print(count)