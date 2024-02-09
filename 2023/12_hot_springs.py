import re

path = 'inputs\\12_input.txt'
with open(path, 'r') as file:
    lines = file.readlines()

arr, arr5 = [], []
for line in lines:
    n = re.findall(r"\d+\d|\d", line)
    nums = []
    for i in n:
        nums.append(int(i))

    arr.append([re.findall(r"([\D:]+) ", line)[0], nums])
    arr5.append([((re.findall(r"([\D:]+) ", line)[0]+'?')*5)[:-1], nums*5])

def eval(record, criteria):
    line = '.*'
    for n in criteria:
        line += (('#'*n) + '.+')
    line = line[:-1] + '*'

    states, statemp, n = {1: 1}, {}, (sum(criteria)+len(criteria)+1)
    machine = {1: ('.', '#')}
    curr = 2
    for spring in criteria:
        for i in range(spring):
            machine[curr] = ('#') if i!=spring-1 else ('.')
            curr+=1
        machine[curr] = ('.', '#')
        curr+=1
    machine.update({curr-1: ('.')})

    for r in record:
        for state in states:
            nextate = state+1 if state<n else state
            if state not in statemp: statemp[state] = 0
            if nextate not in statemp: statemp[nextate] = 0

            if r in machine[state]:
                if r=='#': statemp[nextate]+=states[state]
                if r=='.': statemp[state if len(machine[state])==2 else nextate]+=states[state]
            
            if r=='?':
                if len(machine[state])==2:
                    statemp[state]+=states[state]
                    statemp[nextate]+=states[state]
                if len(machine[state])==1: statemp[nextate]+=states[state]
        
        if statemp[min(list(statemp.keys()))]==0: del statemp[min(list(statemp.keys()))]
        if statemp[max(list(statemp.keys()))]==0: del statemp[max(list(statemp.keys()))]
        states = statemp.copy()
        statemp = {}

    if n not in states: states[n] = 0
    if n-1 not in states: states[n-1] = 0
    return states[n] + states[n-1]

tot = 0
for a in arr:
    tot+=eval(a[0], a[1])

print("Part 1:", tot)

tot = 0
for a in arr5:
    tot+=eval(a[0], a[1])

print("Part 2:", tot)