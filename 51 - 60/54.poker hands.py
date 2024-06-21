f=open("54.poker.txt","r")
l=f.readlines()
lis=[]
for i in l:
    lis.append(i[:-1].split(" "))          #creating each hand of 2 players
order=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]       #order of priority
def royalflush(hand):
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        for i in order[-5:]:
            if i not in (hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]):
                return straightflush(hand)
        return [10,0]
    return straightflush(hand)
def straightflush(hand):
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
        for n in range(len(l)):
            l[n]=order.index(l[n])
        l.sort()
        for num in range(1,5):
            if l[num]!=l[num-1]+1:
                return fourofakind(hand)
        return [9,l[4]]
    return fourofakind(hand)
def fourofakind(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    for card in l:
        if l.count(card)==4:
            return [8,order.index(card)]
    return fullhouse(hand)
def fullhouse(hand):
    if threeofakind(hand)[0]==4 and onepair(hand)[0]==2:
        return [7,threeofakind(hand)[1]]
    return flush(hand)
def flush(hand):
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
        for n in range(len(l)):
            l[n]=order.index(l[n])
        l.sort()
        return [6,l[4]]
    return straight(hand)
def straight(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    for n in range(len(l)):
        l[n]=order.index(l[n])
    l.sort()
    for num in range(1,5):
        if l[num]!=l[num-1]+1:
            return threeofakind(hand)
    return [5,l[4]]
def threeofakind(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    for card in l:
        if l.count(card)==3:
            return [4,order.index(card)]
    return twopairs(hand)
def twopairs(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    x=list(l)
    for card in l:
        if x.count(card)==2:
            x.remove(card)
            x.remove(card)
            for card1 in x:
                if x.count(card1)==2:
                    return [3,max(order.index(card),order.index(card1))]
    return onepair(hand)
def onepair(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    for card in l:
        if l.count(card)==2:
            return [2,order.index(card)]
    return [1,0]
def highcard(hand):
    l=[hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    for n in range(len(l)):
        l[n]=order.index(l[n])
    l.sort()
    return l[4]
win1=0
for hand in lis:
    hand1=hand[:5]
    hand2=hand[5:]
    p1=royalflush(hand1)
    p2=royalflush(hand2)
    if p1[0]>p2[0]:
        win1+=1
    elif p1[0]==p2[0]:
        if p1[1]>p2[1]:
            win1+=1
        elif p1[1]==p2[1]:
            if highcard(hand1)>highcard(hand2):
                win1+=1
print(win1)