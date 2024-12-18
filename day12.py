

from collections import deque


f = open("d12.txt", "r")

lines = f.readlines()

d = []

for l in lines:
    d.append([x for x in l.strip()])


m = len(d)
n = len(d[0])



cache = set()
res1 = 0
res2 = 0
for i in range(m):
    for j in range(n):
        if (i, j) in cache:
            continue
        
        q = deque([(i, j)])
        area = 0
        perim = 0

        perims = {}
        while q:
            x, y = q.popleft()

            if (x, y) in cache:
                continue
            cache.add((x, y))
            area += 1
            
            for nx, ny in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                ni = x + nx
                nj = y + ny

                if 0 <= ni < m and 0 <= nj < n and d[i][j] == d[ni][nj]:
                    q.append((ni, nj))
                else:
                    perim += 1
                    if (nx, ny) not in perims:
                        perims[(nx, ny)] = set()

                    perims[(nx, ny)].add((x, y))


        sid = 0

        for k, vs in perims.items():
            s_p = set()
            print(vs)
            for r,c in vs:
                if (r, c) not in s_p:
                    sid += 1
                    q = deque([(r, c)])

                    while q:
                        x, y = q.popleft()

                        if (x, y) in s_p:
                            continue
                        s_p.add((x, y))

                        for nx, ny in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                            ni = x + nx
                            nj = y + ny
                            if (ni, nj) in vs:
                                q.append((ni, nj))
        print("\n")
        res1 += (area * perim)
        res2 += (sid * area)


print(res1)
print(res2)