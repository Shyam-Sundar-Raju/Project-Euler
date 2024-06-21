count=1      #1 count for 200p coin
for c100 in range(3):   #loopes through the coins with their maximum number of coins as range
    if 100*c100==200:   #inside each loop it breaks if sum=200 and updates count
        count+=1
        break
    elif 100*c100>200:  #inside each loop it breaks if sum>200
        break
    for c50 in range(5):
        if 100*c100+50*c50==200:
            count+=1
            break
        elif 100*c100+50*c50>200:
            break
        for c20 in range(11):
            if 100*c100+50*c50+20*c20==200:
                count+=1
                break
            elif 100*c100+50*c50+20*c20>200:
                break
            for c10 in range(21):
                if 100*c100+50*c50+20*c20+10*c10==200:
                    count+=1
                    break
                elif 100*c100+50*c50+20*c20+10*c10>200:
                    break
                for c5 in range(41):
                    if 100*c100+50*c50+20*c20+10*c10+5*c5==200:
                        count+=1
                        break
                    elif 100*c100+50*c50+20*c20+10*c10+5*c5>200:
                        break
                    for c2 in range(101):
                        if 100*c100+50*c50+20*c20+10*c10+5*c5+2*c2==200:
                            count+=1
                            break
                        elif 100*c100+50*c50+20*c20+10*c10+5*c5+2*c2>200:
                            break
                        for c1 in range(201):
                            if 100*c100+50*c50+20*c20+10*c10+5*c5+2*c2+1*c1==200:     #this is done for all 7 coins except 200p
                                count+=1
                                break
                            elif 100*c100+50*c50+20*c20+10*c10+5*c5+2*c2+1*c1>200:
                                break
print(count)