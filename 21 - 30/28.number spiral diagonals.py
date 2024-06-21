sum=1001*1001          #instead of finding in a matrix this is finding in a linear set of numbers
wrt=1001*1001          #this is the last digit of the spiral and is also a point
skip=1000              #this is used to keep on decreasing the distance between 2 points
while skip>0:          #execute till skip = 0
    for _ in range (4):   #for each skip the points is changed 4 times, as in the spiral one can see the skip value is same between 5 points ,ex:25,21,17,13,9 ,here 25 is already added to sum in previous skip loop
        wrt-=skip         #1001x1001 is already added to sum , so the wrt is updated first and then added to sum for 4 loop
        sum+=wrt       
    skip-=2               #from observing the spiral ,it is clear that skip value decreases by 2
print(sum)

#in this comment points mean the number lying in the diagonal of the square spiral