suos,sosu=0,0
for i in range(101):
    sosu+=i
    suos+=i**2     #sum of square
sosu=sosu**2       #square of sum
print(sosu-suos)   #difference
