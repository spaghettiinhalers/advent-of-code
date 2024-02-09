import re

path = 'inputs\\09_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

histories = []
for line in lines:
    n = re.findall(r"-\d+\d|-\d|\d+\d|\d", line)
    h = []
    for num in n:
        h.append(int(num))
    histories.append(h)

def nextSeq(nums):
    arr = []
    for i in range(len(nums)-1):
        arr.append(nums[i+1]-nums[i])
    return arr
            
def checkEq(nums):
    if len(list(dict.fromkeys(nums)))==1: return False
    else: return True

tot = 0
for history in histories:
    if checkEq(history)==False: tot+=history[0]
    else:
        seqs = []
        nums = []
        for h in history:
            nums.append(h)
        seqs.append(nums)
        
        while checkEq(nums)==True:
            nums = nextSeq(nums)
            seqs.append(nums)
        
        t = 0
        for seq in seqs:
            t+=seq[-1]
        tot+=t

print("Part 1:", tot)

tot = 0
for history in histories:
    if checkEq(history)==False: tot+=history[0]
    else:
        seqs = []
        nums = []
        for h in history:
            nums.append(h)
        seqs.append(nums)
        
        while checkEq(nums)==True:
            nums = nextSeq(nums)
            seqs.append(nums)
        
        t = 0
        for i in range(len(seqs)):
            t = seqs[(len(seqs)-1-i)][0] - t
        tot+=t

print("Part 2:", tot)