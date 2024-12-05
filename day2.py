from collections import Counter
from heapq import heappush, heappop

f = open("day2.txt", "r")

lines = f.readlines()

def is_good(xs):
    inc_or_dec = (xs==sorted(xs) or xs==sorted(xs,reverse=True))
    ok = True
    for i in range(len(xs)-1):
        diff = abs(xs[i]-xs[i+1])
        if not 1<=diff<=3:
            ok = False
    return inc_or_dec and ok

p1 = 0
p2 = 0
for line in lines:
    xs1 = list(map(int, line.split()))
    if is_good(xs1):
        p1 += 1

    good = False
    for j in range(len(xs1)):
        xs = xs1[:j] + xs1[j+1:]
        if is_good(xs):
            good = True
    if good:
        p2 += 1
print(p1)
print(p2)