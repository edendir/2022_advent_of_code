with open("./day3.txt") as f:
    inp = f.read().split('\n')

vals = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

rucksack = 0

for pack in inp:
    pocket1 = pack[:len(pack) // 2]
    pocket2 = pack[len(pack) // 2:]

    intersection = set(pocket1).intersection(set(pocket2))
    for i in intersection:
        rucksack += 1 + vals.index(i)

print(rucksack)

group = 0

for i in range(0, len(inp), 3):
    try:
        temp = set(inp[i]).intersection(set(inp[i + 1]).intersection(set(inp[i + 2])))
    except:
        continue
    for j in temp:
        group += 1 + vals.index(j)

print(group)
