from collections import deque
from functools import cache
from itertools import product


f = open("day21.txt", "r")


codes = f.read().split("\n")

numerical = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
directional = [
    [None, "^", "A"],
    ["<", "v", ">"]
]



def compute_seqs(keypad):
    cache = {}

    for x in range(len(keypad)):
        for y in range(len(keypad[x])):
            if keypad[x][y] is not None:
                cache[keypad[x][y]] = (x,y)
    
    seq = {}

    for x in cache:
        for y in cache:
            if x == y:
                seq[(x, y)] = "A"
                continue
            poss = []
            q = deque([(cache[x], "")])
            opt = float('inf')

            while q:
                (px, py), moves = q.popleft()
                
                for nx, ny, nc in [(px-1, py, "^"), (px+1,py, "v"), (px, py+1, ">"), (px, py-1, "<")]:
                    if nx < 0 or ny < 0 or nx >= len(keypad) or ny >= len(keypad[0]):
                        continue
                    if keypad[nx][ny] is None:
                        continue
                    if keypad[nx][ny] == y:
                        if opt < len(moves) + 1:
                            break
                        opt = len(moves) + 1
                        poss.append(moves+nc +"A")
                    else:
                        q.append(((nx, ny), moves + nc))
                else:
                    continue
                break
            seq[(x, y)] = poss

    return seq

def solve(str, seqs):
    options = [seqs[(x, y)] for x,y in zip("A" + str, str)]
    return ["".join(x) for x in product(*options)]

num_seq = compute_seqs(numerical)

dir_seq = compute_seqs(directional)

dir_len = {k: len(v[0]) for k, v in dir_seq.items()}
print(dir_len)
@cache
def compute_len(se, d = 25):
    if d == 1:
        return sum(dir_len[(x ,y)] for x, y in zip("A" + se, se))
    l= 0
    for x, y in zip("A" + se, se):
        l += min(compute_len(subse, d-1) for subse in dir_seq[(x, y)])
    return l


res = 0
for c in codes:
    inp = solve(c, num_seq)
    print(inp)
    len = min(map(compute_len, inp))
    res += len * int(c.split("A")[0])
print(res)