path = 'inputs\\10_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

ref = {'|':("n", "s"), '-':("e", "w"), 'L':("n", "e"), 'J':("n", "w"), '7':("s", "w"), 'F':("s", "e"), '.':(), 'S':("n", "e", "w", "s")}
opps = {'n': 's', 'e': 'w', 'w': 'e', 's':'n'}
post = {'|': ['|', 'L', 'F'], 'L': ['J', '7'], 'J': ['|', 'L', 'F'], '7': ['|', 'L', 'F'], 'F': ['J', '7']}
stat = {'|': 'v', 'L': 'u', 'J': 'u', '7': 'd', 'F':'d'}

grid, scoord, i = [], [], 0
for line in lines:
    grid.append([])
    j = 0
    for char in line.strip():
        if char=='S': scoord = [i, j]
        grid[i].append(ref[char])
        j+=1
    i+=1
    

travelled, i, prev = [], 0, 'w'
curr = [scoord[0], scoord[1]+1]
for i in range(19740):
    if i>0 and (curr==[scoord[0], scoord[1]] or curr[0]<0 or curr[1]<0 or curr[0]>140 or curr[1]>139): break
    travelled.append([curr[0], curr[1]])
    
    pipe = grid[curr[0]][curr[1]]
    if pipe[0]==prev: prev = pipe[1]
    else: prev = pipe[0]
    
    if prev=='n': curr[0]-=1
    elif prev=='e': curr[1]+=1
    elif prev=='w': curr[1]-=1
    elif prev=='s': curr[0]+=1
        
    prev = opps[prev]
    i+=1
        
print("Part 1:", int((i+1)/2))

tot = 0
for i in range(len(lines)):
    visited, enclosed, counting, paircheck = [], 0, False, []

    for j in range(len(lines[i])):
        visited.append([i, j])

        if counting==False:
            if [i, j] in travelled and lines[i][j]=='|': counting = True

            if [i, j] in travelled and (lines[i][j]=='L' or lines[i][j]=='J' or lines[i][j]=='7' or lines[i][j]=='F'):
                paircheck.append(stat[lines[i][j]])
                if len(paircheck)==2:
                    counting = not counting if (paircheck[0]!=paircheck[1]) else counting
                    paircheck = []
                
        elif counting==True:
            if [i, j] in travelled and lines[i][j]=='|': counting = False

            if [i, j] in travelled and (lines[i][j]=='L' or lines[i][j]=='J' or lines[i][j]=='7' or lines[i][j]=='F'):
                paircheck.append(stat[lines[i][j]])
                if len(paircheck)==2:
                    counting = not counting if (paircheck[0]!=paircheck[1]) else counting
                    paircheck = []
                
        if counting==True and [i, j] not in travelled: enclosed+=1
            
    tot+=enclosed
            
print("Part 2:", tot-1)