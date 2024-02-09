path = 'inputs\\11_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

rows, cols, g = [], [], []

i = 0
for line in lines:
    if '#' not in line: rows.append(i)
    j = 0
    for char in line:
        if char=='#': g.append([i, j])
        j+=1
    i+=1

i = 0
for j in range(len(lines)):
    check = []
    for line in lines:
        check.append(line[j])
    if '#' not in check: cols.append(i)
    i+=1

    
def getDs(rows, cols, g, n):
    Ds = 0
    for i in range(len(g)):
        r, c = 0, 0
        for row in rows:
            if row>min(g[n][0], g[i][0]) and row<max(g[n][0], g[i][0]): r+=1
        for col in cols:
            if col>min(g[n][1], g[i][1]) and col<max(g[n][1], g[i][1]): c+=1
        
        Ds+=(abs(g[n][0]-g[i][0]) + abs(g[n][1]-g[i][1]) + r + c)
    return Ds

def getbigDs(rows, cols, g, n):
    Ds = 0
    for i in range(len(g)):
        r, c = 0, 0
        for row in rows:
            if row>min(g[n][0], g[i][0]) and row<max(g[n][0], g[i][0]): r+=1
        for col in cols:
            if col>min(g[n][1], g[i][1]) and col<max(g[n][1], g[i][1]): c+=1
        
        Ds+=(abs(g[n][0]-g[i][0]) + abs(g[n][1]-g[i][1]) + (999999*(r + c)))
    return Ds

sum = 0
for i in range(len(g)):
    sum+=getDs(rows, cols, g, i)

print("Part 1:", int(sum/2))

sum = 0
for i in range(len(g)):
    sum+=getbigDs(rows, cols, g, i)

print("Part 2:", int(sum/2))