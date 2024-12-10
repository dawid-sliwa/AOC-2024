from collections import defaultdict

f = open("day8.txt", "r")


lines = f.readlines()


d = []
for l in lines:
    d.append([x for x in l.strip()])

m = len(d)
n = len(d[0])

res = set()

nodes = defaultdict(list)
for i in range(m):
    for j in range(n):
        c = d[i][j]
        if c != '.':
            nodes[c].append((i, j))

res2 = set()
for r in range(m):
    for c in range(n):
        for k, v in nodes.items():
            for x1,y1 in v:
                for x2,y2 in v:
                    if (x1,y1) != (x2,y2):
                        c1 = (2*x2-x1, 2*y2-y1)
                        c2 = (2*x1-x2, 2*y1-y2)
                        
                        if 0 <= c1[0] < m and 0 <= c1[1] < n:
                            res.add(c1)
                        if 0 <= c2[0] < m and 0 <= c2[1] < n:
                            res.add(c2)

                        dr1 = r - x1
                        dr2 = r - x2
                        dc1 = c - y1
                        dc2 = c - y2

                        if (dr1 * dc2 == dr2 * dc1):
                            res2.add((r, c))


                
                
                

print(len(res))
print(len(res2))