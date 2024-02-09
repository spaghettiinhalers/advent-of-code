import re

path = 'inputs\\15_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

strs = re.findall(r"[\w]+=+\d|\w+-", lines[0])
box = []
for i in range(256):
    box.append([])

def getRes(string):
    n = 0
    for char in string:
        n=(((n+ord(char))*17)%256)
    return n

tot = 0
for string in strs:
    tot+=getRes(string)

print("Part 1:", tot)

for string in strs:
    if '=' in string:
        added = False
        lens, lnum = string[:-2], string[-1]
        for i in range(len(box[getRes(lens)])):
            if box[getRes(lens)][i][0]==lens:
                box[getRes(lens)][i][1] = lnum
                added = True
        if added==False:
            box[getRes(lens)].append([lens, lnum])
            
    elif '-' in string:
        deled = False
        lens = string[:-1]
        for i in range(len(box[getRes(lens)])):
            if box[getRes(lens)][i][0]==lens: box[getRes(lens)][i] = 0
        while 0 in box[getRes(lens)]:
            box[getRes(lens)].remove(0)

tot = 0
for b in range(len(box)):
    for i in range(len(box[b])):
        tot+=((b+1)*(i+1)*int(box[b][i][1]))

print("Part 2:", tot)