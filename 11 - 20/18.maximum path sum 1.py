x="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""      #the number
lis=[]          #has all the number in one list
tlis=[]
for i in range(len(x)):
    if x[i]==" " or x[i]=="\n":
        if x[i-2]=="0":
            lis.append(x[i-1:i])
        else:
            lis.append(x[i-2:i])
lis.append(x[-2::])
lis1=[]          #this is the final list of lists containing elements
linecount=x.count("\n")+1
for line in range(1,linecount+1):
    lis2=[]
    for dig in range(line):
        lis2.append(int(lis[0]))
        lis.pop(0)
    lis1.append(lis2)
print(lis1)            #final list, the real code starts from next line
for row in lis1[-2::-1]:     #takes one row at a time from the bottom and adds the bigger of 2 number to the upper row number
    rind=lis1.index(row)     #by this method at last the top number will be the max path sum
    for col in row:
        cind=row.index(col)
        lis1[rind][cind]+=max([lis1[rind+1][cind],lis1[rind+1][cind+1]])    #the number is added to the bigger number of the 2 numbers below it.
print(lis1[0])