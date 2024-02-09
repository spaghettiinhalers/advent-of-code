path = 'inputs\\14_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

grid, i = [], 0
for line in lines:
    grid.append([])
    j = 0
    for char in line.strip():
        grid[i].append(char)
        j+=1
    i+=1
    
def getRocks(grid):
    arr, i = [], 0
    for row in grid:
        j = 0
        for n in row:
            if n=='O': arr.append([i, j])
            j+=1
        i+=1
    return(arr)

def tiltN(grid):
    rock = getRocks(grid)
    for r in rock:
        pos = [r[0], r[1]]
        if r[0]>0:
            while pos[0]>0 and grid[pos[0]-1][pos[1]]=='.':
                pos = [pos[0]-1, pos[1]]
        grid[r[0]][r[1]] = '.'
        grid[pos[0]][pos[1]] = 'O'
    return(grid)

def tiltW(grid):
    rock = getRocks(grid)
    for r in rock:
        pos = [r[0], r[1]]
        if r[1]>0:
            while grid[pos[0]][pos[1]-1]=='.' and pos[1]>0:
                pos = [pos[0], pos[1]-1]
        grid[r[0]][r[1]] = '.'
        grid[pos[0]][pos[1]] = 'O'
    return(grid)

def tiltS(grid):
    rock = getRocks(grid)
    rock.reverse()
    for r in rock:
        pos = [r[0], r[1]]
        if r[0]<(len(grid)-1):
            while pos[0]<(len(grid)-1) and grid[pos[0]+1][pos[1]]=='.':
                pos = [pos[0]+1, pos[1]]
        grid[r[0]][r[1]] = '.'
        grid[pos[0]][pos[1]] = 'O'
    return(grid)

def tiltE(grid):
    rock = getRocks(grid)
    rock.reverse()
    for r in rock:
        pos = [r[0], r[1]]
        if r[1]<(len(grid[0])-1):
            while pos[1]<(len(grid[0])-1) and grid[pos[0]][pos[1]+1]=='.':
                pos = [pos[0], pos[1]+1]
        grid[r[0]][r[1]] = '.'
        grid[pos[0]][pos[1]] = 'O'
    return(grid)

grid1, tot = tiltN(grid), 0
for i in range(len(grid1)):
    os = 0
    for n in grid1[i]:
        if n=='O': os+=1
    tot+=(os*(len(grid1)-i))

print("Part 1:", tot)

grids, grid2 = [], grid.copy()
for i in range(1000000000):
    grid2 = tiltE(tiltS(tiltW(tiltN(grid2))))
    if grid2 in grids:
        j = 0
        for g in grids:
            if g==grid2: break
            j+=1
        grid2 = grids[((1000000000-j)%(i-j))+j-1]
        break
    else:
        grids.append([])
        for x in range(len(grid2)):
            grids[i].append([])
            for y in range(len(grid2[0])):
                grids[i][x].append(grid2[x][y])

tot = 0
for i in range(len(grid2)):
    os = 0
    for n in grid2[i]:
        if n=='O': os+=1
    tot+=(os*(len(grid2)-i))

print("Part 2:", tot)