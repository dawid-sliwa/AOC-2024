

from collections import deque


f = open("day10.txt", "r")

lines = f.readlines()


d = []

for l in lines:
    d.append([int(x) for x in l.strip()])

m = len(d)
n = len(d[0])

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def solve(x, y):
    deq = deque()
    deq.append((x, y, 0))
    res = set()
    res2 = 0

    while deq:
        x, y, num = deq.popleft()
        if num == 9:
            res.add((x, y))
            res2 += 1
            continue
        for i, j in dirs:
            nx = x + i
            ny = y + j
            if 0 <= nx < m and 0 <= ny < n and d[nx][ny] == num + 1:
                deq.append((nx, ny, num + 1))

    return (len(res) , res2)


res1 = 0
res2 = 0
for i in range(m):
    for j in range(n):
        if d[i][j] == 0:
            (a1, a2) = solve(i, j)
            res1 += a1
            res2 += a2


print(res1)
print(res2)