from collections import Counter
from heapq import heappush, heappop

f = open("day4.txt", "r")

lines = f.readlines()

d = [[c for c in l.strip()] for l in lines]

res = 0
m = len(d)
n = len(d[0])

# part 1
for i in range(m):
    for j in range(n):
        # print(res, i, j)
        # TOP
        if i >= 3 and d[i][j] == "X" and d[i-1][j] == "M" and d[i-2][j] == "A" and d[i-3][j] == "S":
            res += 1
        # TOP RIGHT
        if i >= 3 and j < n - 3 and d[i][j] == "X" and d[i-1][j+1] == "M" and d[i-2][j+2] == "A" and d[i-3][j+3] == "S":
            res += 1
        # RIGHT
        if j < n - 3 and d[i][j] == "X" and d[i][j+1] == "M" and d[i][j+2] == "A" and d[i][j+3] == "S":
            res += 1
        # DOWN RIGHT
        if i < m - 3 and j < n - 3 and d[i][j] == "X" and d[i+1][j+1] == "M" and d[i+2][j+2] == "A" and d[i+3][j+3] == "S":
            res += 1
        # DOWN
        if i < m - 3 and d[i][j] == "X" and d[i+1][j] == "M" and d[i+2][j] == "A" and d[i+3][j] == "S":
            res += 1
        # DOWN LEFT
        if i < m - 3 and j >= 3 and d[i][j] == "X" and d[i+1][j-1] == "M" and d[i+2][j-2] == "A" and d[i+3][j-3] == "S":
            res += 1
        # LEFT
        if j >= 3 and d[i][j] == "X" and d[i][j-1] == "M" and d[i][j-2] == "A" and d[i][j-3] == "S":
            res += 1
        # LEFT TOP
        if j >= 3 and i >= 3 and d[i][j] == "X" and d[i-1][j-1] == "M" and d[i-2][j-2] == "A" and d[i-3][j-3] == "S":
            res += 1
        

print(res)

# part2
res2 = 0

# TL TR DR DL
hs = set(["MMSS", "SMMS", "SSMM", "MSSM"])

def check(s: str):
    return s in hs

for i in range(m):
    for j in range(n):
        if i < m - 2 and j < n - 2 and d[i][j] == "S" and d[i+1][j+1] == "A" and d[i+2][j+2] == "M" and d[i+2][j] == "S" and d[i][j+2] == "M":
            res2 += 1
        if i < m - 2 and j < n - 2 and d[i][j] == "S" and d[i+1][j+1] == "A" and d[i+2][j+2] == "M" and d[i+2][j] == "M" and d[i][j+2] == "S":
            res2 += 1

        if i < m - 2 and j < n - 2 and d[i][j] == "M" and d[i+1][j+1] == "A" and d[i+2][j+2] == "S" and d[i+2][j] == "M" and d[i][j+2] == "S":
            res2 += 1

        if i < m - 2 and j < n - 2 and d[i][j] == "M" and d[i+1][j+1] == "A" and d[i+2][j+2] == "S" and d[i+2][j] == "S" and d[i][j+2] == "M":
            res2 += 1
        

print(res2)