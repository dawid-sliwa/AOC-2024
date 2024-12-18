from typing import List


f = open("day11.txt", "r")

lines = f.readlines()
d = lines[0].strip().split(" ")
d = [int(x) for x in d]


cache = {}

def process_stone(s, n):
    if n == 75:
        return 1

    if (s, n) in cache:
        return cache[(s, n)]
    
    res = 0
    if s == 0:
        res = process_stone(1, n+1)    
    elif (conv := str(s)) and len(conv) % 2 == 0:
        p1, p2 = conv[0:len(conv)//2], conv[len(conv)//2:len(conv)]
        
        res += process_stone(int(p1), n+1)
        res += process_stone(int(p2), n+1)
    else:
        res = process_stone(s * 2024, n+1)

    cache[(s, n)] = res
    return res

res1 = 0

for i in range(len(d)):
    res1 += process_stone(d[i], 0)

print(res1)