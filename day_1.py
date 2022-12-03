with open("./day1.txt") as f:
    inp = f.read()

elves = []
for elf in inp.split('\n\n'):
    elves.append(sum(map(int, elf.split())))

elves.sort()
print(elves[-1])
print(sum(elves[-3:]))