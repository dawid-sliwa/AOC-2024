

import re


f = open("day13.txt", "r")

lines = f.read().strip()


d = [l.strip() for l in lines]
idx = 0 

def solve(ax, ay, bx, by, prizex, prizey):
    won = False
    min_res = float('inf')

    for na in range(101):
        if (prizex - ax*na) % bx == 0:
            nb = (prizex - ax*na) // bx
            if nb >= 0:
                if (ay * na + by * nb) == prizey:
                    cost = 3 * na + nb
                    if cost < min_res:
                        min_res = min(cost, min_res)
                        won = True
    return min_res if won else 0

machines = lines.split('\n\n')
res1 = 0
for i,machine in enumerate(machines):

    a,b,prize = machine.split('\n')
   
    aw = a.split()
    ax = int(aw[2].split('+')[1].split(',')[0])
    ay = int(aw[3].split('+')[1].split(',')[0])
    bw = b.split()
    bx = int(bw[2].split('+')[1].split(',')[0])
    by = int(bw[3].split('+')[1].split(',')[0])
    pw = prize.split()
    px = int(pw[1].split('=')[1].split(',')[0])
    py = int(pw[2].split('=')[1])

    res1 += solve(ax,ay,bx,by,px,py)

print(res1)