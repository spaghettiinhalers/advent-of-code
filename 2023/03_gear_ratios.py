import re

path = 'inputs\\03_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

grid = []
i = 0
for line in lines:
    grid.append([])
    for char in line.strip():
        grid[i].append(char)
    i+=1

nums = []
for line in lines:
    temp = re.findall(r"\d+\d|\d", line)
    inttemp = []
    for thing in temp:
        inttemp.append(int(thing))
    nums.append(inttemp)

foo = []
for line in lines:
    foo.append([])
    j = 0
    for char in line:
        if (char.isdigit() and not line[j-1].isdigit() and j != 0) or (j == 0 and char.isdigit()):
            foo[-1].append(j)
        j+=1

parts = []
i = 0
for row in nums:
    parts.append([])
    j = 0
    for num in row:
        parts[i].append((nums[i][j],foo[i][j], len(str(nums[i][j]))))
        j+=1
    i+=1

parts2 = {}
i = 0
for row in parts:
    for part in row:
        for j in range(part[2]):
            parts2[(i, part[1]+j)] = part[0]
    i+=1

gears = []
i = 0
for line in lines:
    j = 0
    for char in line:
        if char == '*': gears.append((i, j))
        j+=1
    i+=1 
    
def symbolAdj(num, row, col, len):
    arr = []
    
    try: arr.append(grid[row][col-1])
    except: arr.append('.')
    try: arr.append(grid[row][col+len])
    except: arr.append('.')
    
    for i in range(len+2):
        try: arr.append(grid[row-1][col+i-1])
        except: arr.append('.')
    for i in range(len+2):
        try: arr.append(grid[row+1][col+i-1])
        except: arr.append('.')
    for x in arr:
        if x != '.' and not x.isdigit():
            return num
    return 0

def gearAdj(gear):
    row = gear[0]
    col = gear[1]
    parts = []
    adj = 0
    
    if (row-1, col-1) in parts2: parts.append(parts2[(row-1, col-1)])
    if (row-1, col  ) in parts2: parts.append(parts2[(row-1, col  )])
    if (row-1, col+1) in parts2: parts.append(parts2[(row-1, col+1)])
    if (row  , col-1) in parts2: parts.append(parts2[(row  , col-1)])
    if (row  , col+1) in parts2: parts.append(parts2[(row  , col+1)])
    if (row+1, col-1) in parts2: parts.append(parts2[(row+1, col-1)])
    if (row+1, col  ) in parts2: parts.append(parts2[(row+1, col  )])
    if (row+1, col+1) in parts2: parts.append(parts2[(row+1, col+1)])
    
    noDupes = list(dict.fromkeys(parts))
    if len(noDupes) == 2:
        return noDupes[0] * noDupes[1]
    return 0

tot, i = 0, 0
for row in parts:
    for tup in row:
        tot += symbolAdj(tup[0], i, tup[1], tup[2])
    i+=1

print("Part 1:", tot)

tot = 0
for gear in gears:
    tot+=gearAdj(gear)

print("Part 2:", tot)