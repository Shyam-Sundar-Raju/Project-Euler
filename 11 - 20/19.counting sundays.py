leap=[y for y in range(1904,2001,4)]    #list of leap years
count=0                  #count of sundays on 1st of month
day=2                    #2->monday, 1->sunday, 3->tuesday....
d31=[1,3,5,7,8,10,12]    #months containing 31 days
d30=[4,6,9,11]           #months containing 30 days
for year in range(1900,2001):   #calculating from 1900 because it is the reference date given in question 
    for month in range(1,13):
        if month in d31:
            day+=3           #if 31 days the day of week shifts right by 3 days
        elif month in d30:
            day+=2           #if 30 days the day of week shifts right by 2 days
        else:
            if year in leap:  #if not leap the day doesn't change
                day+=1       #if 29 days the day of week shifts right by 1 day
        if day>7:            #this is to make sure day is within 7
            day-=7
        if day==1:           #checking if sunday
            if year!=1900:   #removing all cases in 1900 as results only since 1901 are needed
                count+=1
print(count)