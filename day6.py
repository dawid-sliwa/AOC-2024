f = open("day6.txt", "r")


lines = f.readlines()

d = []
for l in lines:
    d.append([x for x in l.strip()])


idx = [-1, -1]


m = len(d)
n = len(d[0])

# find start
for i in range(m):
    outer_break = False
    for j in range(n):
        if d[i][j] == '^':
            idx = [i, j]
            outer_break = True
            break
    if outer_break:
        break

starting = idx[:]
seen = set()

curr_dir = "U"
seen.add((idx[0], idx[1]))

hs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

def turn_right(s):
    if s == "U":
        return "R"
    if s == "R":
        return "D"
    if s == "D":
        return "L"
    if s == "L":
        return "U"


while True:
    i , j = idx[0], idx[1]
    direction = hs[curr_dir]
    next_i = i + direction[0]
    next_j = j + direction[1]
    if next_i < m and next_j < n and next_i >= 0 and next_j >= 0:
        if d[next_i][next_j] != "#":
            
            seen.add((next_i, next_j))
            idx = [next_i, next_j]
        elif d[next_i][next_j] == "#":
            curr_dir = turn_right(curr_dir)
    else:
        break
# res1
print(len(seen))

res2 = 0
# part2 compute every possibility because i am stupid

for r in range(m):
    for c in range(n):
        seen_nd = set()
        curr_dir = "U"
        idx = starting[:]
        
        while True:
            i , j = idx[0], idx[1]
            direction = hs[curr_dir]
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < m and next_j < n and next_i >= 0 and next_j >= 0:
                if d[next_i][next_j] == "#" or next_i == r and next_j == c:
                    curr_dir = turn_right(curr_dir)
                elif d[next_i][next_j] != "#":         
                    if (next_i, next_j, curr_dir) in seen_nd:
                        res2+=1
                        break
                    seen_nd.add((next_i, next_j, curr_dir))
                    idx = [next_i, next_j]
            else:
                break

print(res2)