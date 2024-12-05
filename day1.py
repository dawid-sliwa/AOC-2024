from collections import Counter
from heapq import heappush, heappop

f = open("day1.txt", "r")

lines = f.readlines()

heap1 = []
heap2 = []

cnt = Counter()

for l in lines:
    first, second = l.split("   ")

    heappush(heap1, first)
    heappush(heap2, second)
    

res1 = 0
while heap1:
    first = heappop(heap1)
    second = heappop(heap2)

    res1 += abs(int(first) - int(second))

print(res1)

res2 = 0

for l in lines:
    first, second = l.split("   ")
    cnt[int(second)] += 1


for l in lines:
    first, second = l.split("   ")
    res2 += int(first) * cnt[int(first)] 


print(res2)