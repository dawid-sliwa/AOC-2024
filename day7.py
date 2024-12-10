import re


f = open("day7.txt", "r")


lines = f.readlines()

# part1
res1 = 0
for l in lines:
    idx = 0
    while l[idx] != ":":
        idx += 1
    
    target = int(l[0:idx])
    idx += 1

    nums = l[idx:len(l)].strip().split(" ")
    nums = [int(x) for x in nums]

    helper = []
    helper.append(nums[0])
    # i was doing sick dont judge
    for i in range(1, len(nums)):
        num = nums[i]
        pos = []
        for c in helper:
            pos.append(c * num)
            pos.append(c + num)
        
        helper.extend(pos)
    
    if target in set(helper):
        res1 += target


def calc(target, arr):
    if len(arr) == 1:
        return arr[0] == target
    if calc(target, [arr[0] + arr[1]] + arr[2:]):
        return True
    if calc(target, [arr[0] * arr[1]] + arr[2:]):
        return True
    if calc(target, [int(str(arr[0]) + str(arr[1]))] + arr[2:]):
        return True
    return False
# print(res1)
# part2
res2 = 0
for l in lines:
    idx = 0
    while l[idx] != ":":
        idx += 1
    
    target = int(l[0:idx])
    idx += 1

    nums = l[idx:len(l)].strip().split(" ")
    nums = [int(x) for x in nums]

    if calc(target, nums):
        res2+=target
print(res2)