from math import *
nfile=open("42.words.txt","r")      #opening text file
r=nfile.readline()                  #readinf txt file
nlis=r.split(",")               #creating list of text
alp="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #for finding position
count=0                    #count of triangle words
def codeofstr(s):          #for calculating the number value of each word
    code=0
    for i in s:
        code+=alp.index(i)
    return code
def istrinum(n):           #finding if a num is triangle
    a = int(sqrt(2*n))
    return 0.5*a*(a+1) == n
for i in nlis:             #accessing each word in lis
    code=codeofstr(i[1:-1])   #the word has 2 quotes ,so to remove one quotes
    if istrinum(code):
        count+=1
print(count)