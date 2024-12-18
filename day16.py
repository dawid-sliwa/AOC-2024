from collections import defaultdict
from heapq import heappush, heappop
f = open("d16.txt", "r")

lines = f.readlines()

d = [l.strip() for l in lines]
d = [[c for c in l] for l in d]
m = len(d)
n = len(d[0])

for i in range(m):
    for j in range(n):
        if d[i][j] == 'S':
            sx,sy = i, j
        if d[i][j] == 'E':
            ex,ey = i, j

angles = {
    0: (-1, 0),
    90: (0, 1),
    180: (1, 0),
    270: (0, -1)
}

DIRS = [(-1,0),(0,1),(1,0),(0,-1)] 

h = []

vis = {}

heappush(h, (0, sx, sy, 1, set([(sx, sy)])))



res = float('inf')
res2 = set()
seen = {}
heap2 = []
while h:
    cost, x, y, angle, path = heappop(h)

    if (x, y, angle) not in vis:
        vis[(x,y,angle)] = cost
    if x == ex and  y == ey:
        res = min(res, cost)
        heappush(heap2, (cost, path))
        continue
    if (x, y, angle) in seen and seen[(x,y,angle)] < cost:
        continue
    seen[(x,y,angle)] = cost
    path.add((x, y))

    mx, my = DIRS[angle]
    nx, ny = x + mx, y + my
    if d[nx][ny] != "#" and 0 <= nx < m and 0 <= ny < n:
        heappush(h, (cost + 1, nx, ny, angle, path.copy()))
    
    heappush(h, (cost + 1000, x, y, (angle + 1) % 4, path.copy()))
    heappush(h, (cost + 1000, x, y, (angle + 3) % 4, path.copy()))

# print(res)

initial_cost, _ = heap2[0]

while heap2 and heap2[0][0] == initial_cost:
    cost, paths = heappop(heap2)
    res2.update(paths)
    
print(len(res2))
cd = d
for x, y in res2:
    cd[x][y] = "O"

for asd in cd:
    print(asd)