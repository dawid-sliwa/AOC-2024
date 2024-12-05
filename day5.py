from collections import defaultdict


f = open("day5.txt", "r")

lines = f.readlines()


# parse rules

idx = 0

hs = defaultdict(set)

while lines[idx] != "\n":
    l = lines[idx]
    first, second = int(l[0:2]), int(l[3:5])
    
    hs[first].add(second)

    idx+= 1
idx += 1
data = []

while idx < len(lines):
    data.append(list(map(int, lines[idx].split(","))))
    idx += 1

res1 = 0

def check(d):
    curr = set()
    for num in d:
        pages = hs[num]

        for p in pages:
            if p in curr:
                return False
        curr.add(num)
    
    return d[len(d)//2]

d2 = []
for d in data:
    curr = set()
    outer_broken = False
    
    c = check(d)
    if c:
        res1 += c
    else:
        d2.append(d)

print(res1)

res2 = 0

from functools import cmp_to_key

def sort_by(x1, x2):
    h1 = hs[x1]
    h2 = hs[x2]

    if x1 in h2:
        return 1
    elif x2 in h1:
        return -1
    else:
        return 0 

for d in d2:
    print(d)
    d.sort(key=cmp_to_key(sort_by))
    print(d)
    res2+=d[len(d)//2]

print(res2)
