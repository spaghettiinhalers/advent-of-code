import re

path = 'inputs\\05_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

seedsStr = re.findall(r"\d+\d|\d", lines[0])
seeds = []
for seed in seedsStr:
    seeds.append(int(seed))

maps = [[],[],[],[],[],[],[]]
rows = [(33,3),(41,38),(42,81),(27,125),(38,154),(13,194),(26,209)]

seedRange, tempRange = [], []
for i in range(int(len(seeds)/2)):
    seedRange.append([seeds[2*i], seeds[2*i] + seeds[2*i+1]])
    tempRange.append([seeds[2*i], seeds[2*i] + seeds[2*i+1]]) 

i = 0
for map in maps:
    for j in range(rows[i][0]):
        n = re.findall(r"\d+\d|\d", lines[rows[i][1]+j])
        maps[i].append([int(n[0])-int(n[1]), int(n[1]), int(n[1])+int(n[2])-1])
    i+=1

def mapRun(map, num):
    for arr in map:
        if num>=arr[1] and num<arr[2]:
            num+=arr[0]
            break
    return num

def findRange(map, range):
    lo = []
    hi = []
    for arr in map:
        if range[0]>=arr[1] and range[0]<=arr[2]: lo = arr
        if range[1]>=arr[1] and range[1]<=arr[2]: hi = arr

    if lo==[] and hi!=[]: lo = [0, 0, hi[1]-1]
    if lo!=[] and hi==[]: hi = [0, lo[2]+1, range[1]]
    if lo==[] and hi==[]:
        lo = [0, 0, range[1]]
        hi = lo
            
    if lo!=hi:
        return[[range[0], lo[2]+lo[0]], [range[1], hi[1]+hi[0]]]
    else:
        return[[range[0], range[1]]]

def getRange(i, maps, ranges):
    arr = []
    for range in ranges:
        new = findRange(maps[i], range)
        for n in new:
            arr.append(n)
    return(arr)

arr = []
for seed in seeds:
    s = seed
    for map in maps:
        s = mapRun(map, s)
    arr.append(s)

print("Part 1:", min(arr))

for i in range(7):
    tempRange = getRange(i, maps, tempRange)

mnn = min(arr)
for a in tempRange:
    for b in a:
        if b<mnn and b>0: mnn = b
print("Part 2:", mnn)

# # PART 2 ALTERNATIVE
# d = []
# for map in maps:
#     for r in map:
#         if r[0]>0 and r[0]<107430936: d.append(r[0])
# d.sort()
# print(d)