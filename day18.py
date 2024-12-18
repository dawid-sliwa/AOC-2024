from collections import deque
from heapq import heappush


f = open("d18.txt", "r")

lines = f.readlines()

m = 6 + 1
n = 6 + 1

d = [["." for _ in range(m)] for _ in range(m)]

moves = [l.strip() for l in lines]


for i in range(len(moves)):
    move = moves[i]
    x, y = move.split(",")
    x, y = int(x), int(y)
    d[y][x] = "#"

    q = deque([(0, 0, 0)])
    dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
    vis = set()
    res = float('inf')
    while q:
        xx, yy, dist = q.popleft()

        if xx == m-1 and yy == n-1:
            if dist < res:
                res = dist
                
            
        if (xx, yy) in vis:
            continue
        vis.add((xx, yy))

        for dir in dirs:
            nx, ny = xx + dir[0], yy + dir[1]

            if 0 <= nx < m and 0 <= ny < n and d[nx][ny] != "#":
                q.append((nx, ny, dist+1))
    if res == float('inf'):
        print(x, y)
        break