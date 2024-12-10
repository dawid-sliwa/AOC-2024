from collections import deque


f = open("day9.txt", "r")


lines = f.readlines()
input_data = lines[0]

initial = []



idx = 0
id = 0

# total = 0
empty_indexes = []
while idx < len(input_data)-1:
    block_size = int(input_data[idx])

    # total += block_size
    empty_size = int(input_data[idx+1])
    

    initial.extend([str(id)] * block_size)
    initial.extend(["."] * empty_size)

    idx += 2
    id += 1

if idx != len(input_data):
    initial.extend([str(id)] * int(input_data[idx]))



i = 0

for i in range(len(initial)):
    if initial[i] == ".":
        empty_indexes.append(i)


full = list(range(len(initial)))

occupied_indexes = list(set(full).difference(set(empty_indexes)))

i = 0
occupied_indexes.reverse()

l = len(initial) - len(occupied_indexes)
new_empty = []
new_occupied = []


while i < l:
    num_idx = occupied_indexes[i]
    empty_idx = empty_indexes[i]
    
    initial[num_idx], initial[empty_idx] = initial[empty_idx], initial[num_idx]
    new_empty.insert(0, num_idx)
    new_occupied.insert(0, empty_idx)
    if empty_idx > num_idx:
        break
        

    i+=1

initial[new_empty[0]], initial[new_occupied[0]] = initial[new_occupied[0]], initial[new_empty[0]]

start = 0
res1 = 0
while initial[start] != ".":
    res1 += start * int(initial[start])
    start += 1

print(res1)
# part2

nums = deque()
spaces = deque()
res = []
file_id = 0
pos = 0
for idx, c in enumerate(input_data):
    if idx % 2 == 0:
        nums.append((pos, int(c), file_id))

        for i in range(int(c)):
            res.append(file_id)
            pos += 1
        file_id += 1
    else:

        spaces.append((pos, int(c)))

        for i in range(int(c)):
            res.append(".")
            pos += 1

print(res)
for (pos, sz, file_id) in reversed(nums):
    for space_i,(space_pos, space_sz) in enumerate(spaces):
        if space_pos < pos and sz <= space_sz:
            for i in range(sz):
                assert res[pos+i] == file_id, f'{res[pos+i]=}'
                res[pos+i] = "."
                res[space_pos+i] = file_id
            spaces[space_i] = (space_pos + sz, space_sz-sz)
            break


start = 0
res2 = 0
while start < len(res):
    if res[start] != '.':
        comp = (start * int(res[start]))
        res2 += comp
    start += 1
print(res2)