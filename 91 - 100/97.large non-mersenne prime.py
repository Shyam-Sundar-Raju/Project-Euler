num=1           #final answer
for x in range(7830457//8):   #2^7830457
    num*=256
    snum=str(num)
    if len(snum)>10:        #only 10 digits are needed, so slicing it
        snum=snum[-10::]
    num=int(snum)
else:
    num=num*2**(7830457%8)   #multiplying the leftover power
    num*=28433
    num+=1
    print(str(num)[-10::])