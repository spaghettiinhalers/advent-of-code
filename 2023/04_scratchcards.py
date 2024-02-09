import re

path = 'inputs\\04_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

cards, nums = [], []
i = 0
for line in lines:
    cards.append([])
    for j in range(30):
        cards[i].append(line[10+j])
    for j in range(74):
        cards[i].append(line[42+j])
    cards[i].append(' ')
    
    j = 0
    for ele in cards[i]:
        if ele==' ': cards[i][j] = '0'
        j+=1

    i+=1

i = 0
for row in cards:
    nums.append([])
    for j in range(35):
        nums[i].append((10*int(row[0+(3*j)]))+int(row[1+(3*j)]))    
    i+=1

tot = 0
for card in nums:
    score = 0
    wins, test = [], []

    for i in range (10):
        wins.append(card[i])
    for i in range(25):
        test.append(card[10+i])
    
    for num in test:
        if num in wins: score+=1
    
    if score!=0: tot += (2**(score-1))

print("Part 1:", tot)

tot = 0
ins = [1]*192
i = 0
for card in nums:
    matches = 0
    wins, test = [], []
    
    for j in range(10):
        wins.append(card[j])
    for j in range(25):
        test.append(card[10+j])\
    
    for num in test:
        if num in wins: matches+=1  
    for j in range(matches):
        ins[i+j+1] = ins[i+j+1] + ins[i]
    
    i+=1

for i in range(192):
    tot += ins[i]

print("Part 2:", tot)