import math
num=math.factorial(100)   #sum of digits in 100!
s=0
for i in str(num):
    s+=int(i)
print(s)
