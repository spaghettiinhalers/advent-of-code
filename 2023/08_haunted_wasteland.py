import re
import math

path = 'inputs\\08_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

steps, nodes, nodel, i = [], {}, [], 0
for line in lines:
    if i==0:
        for char in line:
            if char=='L': steps.append(0)
            if char=='R': steps.append(1)
    if i>1:
        n = re.findall(r"[\w]+", line)
        nodes[str(n[0])] = (n[1], n[2])
        nodel.append(n[0])
    i+=1

curr, i = 'AAA', 0
while curr!='ZZZ':
    curr = nodes[curr][steps[i%len(steps)]]
    i+=1

print("Part 1:", i)

As = []
for node in nodel:
    if node[2]=='A': As.append(node)
Zs = []
for node in nodel:
    if node[2]=='Z': Zs.append(node)

count = []
for A in As:
    curr = A
    i = 0
    while curr not in Zs:
        curr = nodes[curr][steps[i%len(steps)]]
        i+=1
    count.append(i)

m = 1
for c in count:
    m = math.lcm(m, c)
    
print("Part 2:", m)