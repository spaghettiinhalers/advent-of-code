path = 'inputs\\13_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

patterns, i = [[]], 0
for line in lines:
    if line!='\n': patterns[i].append(line.strip())
    else:
        i+=1
        patterns.append([])

def off(arr1, arr2):
    diff = 0
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]: diff+=1
    return diff
        
def checkPattern(pattern):
    for i in range(len(pattern)-1):
        good = True
        valid = min([i+1, len(pattern)-i-1])
        for j in range(valid):
            if pattern[i-j]!=pattern[i+1+j]: good = False
        if good==True: return([0, i])
    
    tP = []
    for i in range(len(pattern[0])):
        tP.append([])
        for j in range(len(pattern)):
            tP[i].append(pattern[j][i])
    for i in range(len(tP)-1):
        good = True
        valid = min([i+1, len(tP)-i-1])
        for j in range(valid):
            if tP[i-j]!=tP[i+1+j]: good = False
        if good==True: return([1, i])

def checkPattern2(pattern):
    for i in range(len(pattern)-1):
        o = 0
        valid = min([i+1, len(pattern)-i-1])
        for j in range(valid):
            o+=off(pattern[i-j], pattern[i+1+j])
        if o==1: return([0, i])
        
    tP = []
    for i in range(len(pattern[0])):
        tP.append([])
        for j in range(len(pattern)):
            tP[i].append(pattern[j][i])
    for i in range(len(tP)-1):
        o = 0
        valid = min([i+1, len(tP)-i-1])
        for j in range(valid):
            o+=off(tP[i-j], tP[i+1+j])
        if o==1: return([1, i])

tot = 0
for pattern in patterns:
    mirror = checkPattern(pattern)
    if mirror[0]==1: tot+=(mirror[1]+1)
    if mirror[0]==0: tot+=(100*(mirror[1]+1))

print("Part 1:", tot)

tot = 0
for pattern in patterns:
    mirror = checkPattern2(pattern)
    if mirror[0]==1: tot+=(mirror[1]+1)
    if mirror[0]==0: tot+=(100*(mirror[1]+1))

print("Part 2:", tot)