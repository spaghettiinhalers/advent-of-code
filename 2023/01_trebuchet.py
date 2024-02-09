import re

path = 'inputs\\01_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

ndict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
         '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

tot = 0
for line in lines:
    stor = []
    for char in line:
        if char.isdigit(): stor.append(int(char))
    if stor!=[]: tot += ((10*stor[0])+(stor[len(stor)-1]))

print("Part 1:", tot)

tot = 0
for line in lines:
    foo = re.compile(r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))")
    nums = [match.group(1) for match in foo.finditer(line)]
    tot += ((10*ndict[nums[0]])+(ndict[nums[len(nums)-1]]))

print("Part 2:", tot)