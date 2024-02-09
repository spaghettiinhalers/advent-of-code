import re

path = 'inputs\\07_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

cardref = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2,}
cardrefJ = {'A':13, 'K':12, 'Q':11, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2,}

def handscore(hand):
    return((hand[0]*(10**8))+(hand[1]*(10**6))+(hand[2]*(10**4))+(hand[3]*(10**2))+(hand[4]))

def handscoreJ(hand):
    return((hand[0]*(10**8))+(hand[1]*(10**6))+(hand[2]*(10**4))+(hand[3]*(10**2))+(hand[4]))

def uniques(list):
    temp = []
    for l in list:
        if l not in temp: temp.append(l)
    return(temp)

hands = []
for line in lines:
    line.strip()
    rank = 0
    for i in range(len(line)-7):
        rank+=(int(line[6+i])*(10**(len(line)-8-i)))
    list=[cardref[line[0]], cardref[line[1]], cardref[line[2]], cardref[line[3]], cardref[line[4]]]
    list.append(rank)
    list.append(handscore(list))
    hands.append(list)

arrhands = [[],[],[],[],[],[],[]]
for row in hands:
    ordd = []
    for i in range(5):
        ordd.append(row[i])
    ordd.sort()
    u = len(uniques(ordd))
    
    if u==1: arrhands[0].append(row)   
    elif u==2:
        if (ordd[0]==ordd[3]) or (ordd[1]==ordd[4]): arrhands[1].append(row)
        else: arrhands[2].append(row)
    elif u==3:
        if (ordd[0]==ordd[2]) or (ordd[1]==ordd[3]) or (ordd[2]==ordd[4]): arrhands[3].append(row)
        else: arrhands[4].append(row)
    elif u==4: arrhands[5].append(row)
    else: arrhands[6].append(row)

dict = {}                                                                  
for group in arrhands:
    for hand in group:
        dict[str(hand[6])] = [hand[0], hand[1], hand[2], hand[3], hand[4], hand[5]]

org = []
for group in arrhands:
    scores = []
    for hand in group:
        scores.append(hand[6])
    scores.sort(reverse=True)
    
    for t in scores:
        org.append(dict[str(t)])

tot, i = 0, 0
for hand in org:
    tot+=(hand[5]*(len(org)-i))
    i+=1

print("Part 1:", tot)

handsJ = []
for line in lines:
    line.strip()
    rank = 0
    for i in range(len(line)-7):
        rank+=(int(line[6+i])*(10**(len(line)-8-i)))
    list=[cardrefJ[line[0]], cardrefJ[line[1]], cardrefJ[line[2]], cardrefJ[line[3]], cardrefJ[line[4]]]
    list.append(rank)
    list.append(handscore(list))
    handsJ.append(list)

arrhandsJ = [[],[],[],[],[],[],[]]
for row in handsJ:
    ordd = []
    for i in range(5):
        ordd.append(row[i])
    ordd.sort()
    
    noJ = []
    Js = 0
    for card in ordd:
        if card==1: Js+=1
        else: noJ.append(card)
    j = len(uniques(noJ))
    
    if Js==0:
        u = len(uniques(ordd))

        if u==1: arrhandsJ[0].append(row)
        elif u==2:
            if (ordd[0]==ordd[3]) or (ordd[1]==ordd[4]): arrhandsJ[1].append(row)
            else: arrhandsJ[2].append(row)
        elif u==3:
            if (ordd[0]==ordd[2]) or (ordd[1]==ordd[3]) or (ordd[2]==ordd[4]): arrhandsJ[3].append(row)
            else: arrhandsJ[4].append(row)
        elif u==4: arrhandsJ[5].append(row)
        else: arrhandsJ[6].append(row)
    
    else:
        if Js==1:
            if j==1: arrhandsJ[0].append(row)
            elif j==2:
                if (noJ[0]==noJ[2]) or (noJ[1]==noJ[3]): arrhandsJ[1].append(row)
                else: arrhandsJ[2].append(row)
            elif j==3: arrhandsJ[3].append(row)
            elif j==4: arrhandsJ[5].append(row)
        if Js==2:
            if j==3: arrhandsJ[3].append(row)
            if j==2: arrhandsJ[1].append(row)
            if j==1: arrhandsJ[0].append(row)
        if Js==3:
            if j==1: arrhandsJ[0].append(row)
            else: arrhandsJ[1].append(row)
        if Js==4 or Js==5: arrhandsJ[0].append(row)
    

dictJ = {}                                            
for group in arrhandsJ:
    for hand in group:
        dictJ[str(hand[6])] = [hand[0], hand[1], hand[2], hand[3], hand[4], hand[5]]

orgJ = []
for group in arrhandsJ:
    scores = []
    for hand in group:
        scores.append(hand[6])
    scores.sort(reverse=True)
    for t in scores:
        orgJ.append(dictJ[str(t)])

totJ, i = 0, 0
for hand in orgJ:
    totJ+=(hand[5]*(len(orgJ)-i))
    i+=1

print("Part 2:", totJ)