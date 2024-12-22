import math
import sys

sys.setrecursionlimit(10**6)


f = open("day22.txt", "r")

nums = f.read().split("\n")
nums = [int(n) for n in nums]
MOD = 16777216

def mix(base, n):
    return base ^ n

def prune(n):
    return n % MOD

def solve(n):
    prices = [n]

    for _ in range(2000):
        n = prune(mix(n, n * 64))
        n = prune(mix(n, n // 32))
        n = prune(mix(n, n * 2048))
        prices.append(n)

    return prices

def genChanges(prices):
    ch = []

    for i in range(1, len(prices)):
        ch.append((prices[i]%10) - (prices[i-1]%10))

    return ch

def traverse(changes, prices):
    temp = {}
    for i in range(len(changes) - 3):
        k1, k2, k3, k4 = changes[i], changes[i + 1], changes[i + 2], changes[i + 3]
        if (k1, k2, k3, k4) not in temp:
            temp[(k1,k2,k3,k4)] = (prices[i + 4] % 10)

    return temp

res1 = 0
cache = {}
for n in nums:
    prices = solve(n)
    res1 += prices[2000]


    changes = genChanges(prices)
    t = traverse(changes, prices)
    for k, v in t.items():
        if k not in cache:
            cache[k] = v
        else:
            cache[k] += v
    

print(res1)
print(max(cache.values()))