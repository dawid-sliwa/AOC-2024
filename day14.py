f = open("day14.txt", "r")

lines = f.readlines()


m = 103
n = 101

d = [['.' for _ in range(n)] for _ in range(m)]

# part 1 dont judge
def solve(px, py, vx, vy):
    sx, sy = px, py
    for _ in range(100):
        sx = (sx + vx) % (n)
        sy = (sy + vy) % (m)
    
    if d[sy][sx] == '.':
        d[sy][sx] = 1
    else:
        d[sy][sx] += 1

for l in lines:
    l = l.strip()
    ps, vs = l.split(" ")
    
    pv, vv = ps.split("="), vs.split("=")
    pv, vv = pv[1], vv[1]
    
    px,py = pv.split(",")
    vx,vy = vv.split(",")
    solve(int(px), int(py), int(vx), int(vy))


p1 = 0
for i in range(m//2):
    for j in range(n//2):
        if d[i][j] != '.':
            p1 += d[i][j]

p2 = 0

for i in range(m//2):
    for j in range((n//2)+1, n):
        if d[i][j] != '.':
            p2 += d[i][j]

p3 = 0
for i in range((m//2)+1, m):
    for j in range(n//2):
        if d[i][j] != '.':
            p3 += d[i][j]

p4 = 0
for i in range((m//2)+1, m):
    for j in range((n//2)+1, n):
        if d[i][j] != '.':
            p4 += d[i][j]


print(p1*p2*p3*p4)


# part2

d2 = [['.' for _ in range(n)] for _ in range(m)]

for i in range(10000):
    res2 = set()
    for l in lines:
        l = l.strip()
        ps, vs = l.split(" ")
        
        pv, vv = ps.split("="), vs.split("=")
        pv, vv = pv[1], vv[1]
        px,py = pv.split(",")
        vx,vy = vv.split(",")
        
        px, py, vx, vy = int(px), int(py), int(vx), int(vy)

        rx = (px + i * vx) % n
        ry = (py + i * vy) % m
        d[ry][rx] = 1
        res2.add((ry,rx))
        if len(res2) == len(lines):
            print(i)
            break