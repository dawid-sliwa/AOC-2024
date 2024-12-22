from collections import Counter, deque
from heapq import heappush


f = open("day20.txt", "r")

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



m = len(d)
n = len(d[0])
q = deque([(ex, ey, 0)])
nodes = {}
while q:
    x, y, steps = q.popleft()

    if (x, y) in nodes:
        continue
    nodes[(x, y)] = steps
    for dx, dy in [(-1,0), (1,0), (0,-1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and d[nx][ny] != "#":
            q.append((nx, ny, steps+1))




def solve(dd, t = 2):
    q = deque([(sx, sy, 0, None, None, None)])

    vis = set()
    save = 100
    res = set()

    while q:
        x, y, steps, c_s, c_e, c_t = q.popleft()
        if steps >= dd - save:
            continue
        if d[x][y] == "E":
            if c_e is None:
                c_e = (x, y)

            if steps <= dd-save and(c_s, c_e) not in res:
                res.add((c_s, c_e))

        if (x, y, c_s, c_e, c_t) in vis:
            continue
        vis.add((x, y, c_s, c_e, c_t))

        if c_s is None:
            q.append((x, y, steps, (x,y), None, t))

        if c_t is not None and d[x][y] != "#":
            if nodes[(x,y)] <= dd - 100 - steps:
                res.add((c_s, (x, y)))

        if c_t == 0:
            continue
        else:
            for dx, dy in [(-1,0), (1,0), (0,-1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if c_t is not None:
                    if 0 <= nx < m and 0 <= ny < n:
                        q.append((nx,ny, steps+1, c_s, None, c_t - 1))
                
                else:
                    if 0 <= nx < m and 0 <= ny < n and d[nx][ny] != "#":
                        q.append((nx,ny,steps+1, c_s, c_e, c_t))


    return len(res)

dd = nodes[(sx, sy)]

print(solve(dd, 2))
print(solve(dd, 20))