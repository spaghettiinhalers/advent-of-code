import re

path = 'inputs\\02_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

def c(arr, max):
    for str in arr:
        if int(re.findall(r"([\d:]+ )(r|g|b)?", str)[0][0])>max:
            return 1
    return 0

tot, i = 0, 0
for line in lines:
    i+=1
    r = re.findall(r"[\d]+ red?", line)
    g = re.findall(r"[\d]+ green?", line)
    b = re.findall(r"[\d]+ blue?", line)
    if ((c(r, 12)+c(g, 13)+c(b, 14))==0):
        tot+=i

print("Part 1:", tot)

tot = 0
for line in lines:
    r = re.findall(r"[\d]+ red?", line)
    rint = [int(re.findall(r"([\d:]+ )(r|g|b)?", str)[0][0]) for str in r]

    g = re.findall(r"[\d]+ green?", line)
    gint = [int(re.findall(r"([\d:]+ )(r|g|b)?", str)[0][0]) for str in g]

    b = re.findall(r"[\d]+ blue?", line)
    bint = [int(re.findall(r"([\d:]+ )(r|g|b)?", str)[0][0]) for str in b]

    power = max(rint)*max(gint)*max(bint)
    tot+=power

print("Part 2:", tot)