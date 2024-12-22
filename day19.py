

from collections import deque


f = open("day19.txt", "r")

poss, desired = f.read().split("\n\n")

poss = [x for x in poss.split(", ")]
desired = [x for x in desired.split("\n")]

p = set(poss)


cache = {}
def parts(target):
    if target in cache:
        return cache[target]
    res = 0    
    if not target:
        res = 1

    for p in poss:
        if target.startswith(p):
            res += parts(target[len(p):])

    cache[target] = res
    return res

res1 = 0
res2 = 0
for d in desired:
    
    cnt = parts(d)
    if cnt > 0:
        res1 += 1
    res2 += cnt

print(res1)
print(res2)