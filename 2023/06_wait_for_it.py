import re

path = 'inputs\\06_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

t = []
d = []
race2 = []
# short inputs were manually entered

races = []
for i in range(4):
    races.append((t[i], d[i]))

tot = 1
for race in races:
    low, high, i = 0, 0, 0
    for i in range(race[0]):
        dis = (race[0]-i)*i
        if dis>race[1]:
            low = i
            break
    for i in range(race[0]):
        dis = (race[0]-(race[0]-i))*(race[0]-i)
        if dis>race[1]:
            high = race[0] - i
            break
    tot *= (high - low + 1)

print("Part 1:", tot)

low, high, i = 0, 0, 0
for i in range(race2[0]):
    dis = (race2[0]-i)*i
    if dis>race2[1]:
        low = i
        break
for i in range(race2[0]):
    dis = (race2[0]-(race2[0]-i))*(race2[0]-i)
    if dis>race2[1]:
        high = race2[0] - i
        break

print("Part 2:", (high - low + 1))