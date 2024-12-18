from collections import deque


f = open("d15.txt", "r")

cords, moves = f.read().split("\n\n")


d = cords.split("\n")

d = [[c for c in l] for l in d]

m = len(d)
n = len(d[0])

# part1


pos = (-1, -1)
for i in range(m):
    for j in range(n):
        if d[i][j] == '@':
            pos = (i, j)

t = {
    "<": (0, -1),
    ">": (0, 1), 
    "v": (1, 0),
    "^": (-1, 0)
}

def dfs(i,j,mov,am):
    if d[i][j] == "#":
        return (False, am)
    if d[i][j] == ".":
        return (True, am)
    
    mx, my = t[mov]

    return dfs(i+mx, j + my, mov, am + 1)

moves = "".join([s for s in moves.strip().split("\n")])

for c in moves:
    mx, my = t[c]

    nx = pos[0] + mx
    ny = pos[1] + my

    if d[nx][ny] != "#":
        can_move, dist = dfs(nx, ny, c, 0)
        # print(c,can_move, dist)
        if can_move:
            d[pos[0]][pos[1]] = '.'

            pos = nx, ny
            d[nx][ny] = "@"
            sx, sy = nx + mx, ny + my

            while dist > 0:
                d[sx][sy] = 'O'
                dist -= 1
                sx, sy = sx + mx, sy + my
            

res1 = 0
for i in range(m):
    for j in range(n):
        if d[i][j] == "O":
            res1 += (100 * (i) + (j))

print(res1)

# part2

d = cords.split("\n")

d = [[c for c in l] for l in d]
m = len(d)
n = len(d[0])

nd = []
for i in range(m):
    nd.append([])
    for j in range(n):
        c = d[i][j]

        if c == "#":
            nd[i].extend(["#", "#"])
        if c == ".":
            nd[i].extend([".", "."])
        if c == "O":
            nd[i].extend(["[", "]"])
        if c == "@":
            nd[i].extend(["@","."])

d = nd
m = len(d)
n = len(d[0])

pos = (-1, -1)
for i in range(m):
    for j in range(n):
        if d[i][j] == '@':
            pos = (i, j)

for asd in d:
    print(asd)
print("\n")


for c in moves:
    mx, my = t[c]

    q = deque([pos])

    cont = False
    vis = set()
    while q:
        x, y = q.popleft()
        if (x, y) in vis:
            continue
        vis.add((x,y))
        nx, ny = x + mx, y + my
        # print(nx, ny)
        if d[nx][ny] == "#":
            cont = True
            break
        elif d[nx][ny] == "[" or d[nx][ny] == "]":
            vis.add((nx, ny))
            q.append((nx, ny))
            if d[nx][ny] == "[":
                vis.add((nx, ny+1))
                q.append((nx, ny+1))
            if d[nx][ny] == "]":
                vis.add((nx, ny-1))
                q.append((nx, ny-1))


    if cont:
        continue

    new_d = [[d[i][j] for j in range(n)] for i in range(m)]
    for x, y in vis:
        new_d[x][y] = '.'
    for x, y in vis:
        new_d[x+mx][y+my] = d[x][y]
    d = new_d

    pos = (pos[0] + mx, pos[1] + my)

    for asd in d:
        print(asd)
    print("\n")

res2 = 0

for i in range(m):
    for j in range(n):
        if d[i][j] == "[":
            res2 += (100 * i + j)
print(res2)