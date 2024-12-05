from collections import Counter
from heapq import heappush, heappop

f = open("day3.txt", "r")

lines = f.readlines()
s = ""
for l in lines:
    s += l

goods = set([",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

def check(s: str):
    idx = 0

    while idx < len(s) - 1 and s[idx] in goods:
        idx += 1
    if s[idx] == ")":
        return True
    else:
        return False
    

t = 0

idx = 0
res = 0
enabled = True
while idx < len(s) - 4:
    # print(s[idx: idx+7])
    if s[idx:idx+4] == "do()":
        enabled = True
    elif s[idx:idx+7] == "don't()":
        print("asd")
        t += 1
        enabled = False 
    elif s[idx:idx+4] == 'mul(' and check(s[idx+4:idx+12]):
        first_start_idx = idx + 4
        first_end_idx = idx + 4
        while s[first_end_idx] != ",":
            first_end_idx += 1

        first = int(s[first_start_idx:first_end_idx])
        
        second_start_idx = first_end_idx + 1
        second_end_idx = first_end_idx + 1

        while s[second_end_idx] != ")":
            second_end_idx += 1
        second = int(s[second_start_idx:second_end_idx])
        # print(first, second)
        if enabled:
            res += (first * second)
    else:
        pass
    idx+=1

print(res)
print(t)