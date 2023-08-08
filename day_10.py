import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "day10.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

cycle = 0
reg = 1
signal = 0

def signal_strength(cycle, x):
    global signal
    if cycle in (20, 60, 100, 140, 180, 220):
        return cycle*x
    return 0
    
for line in lines:
    if line.startswith('noop'):
        cycle += 1
        signal_strength(cycle, 0)
    elif line.startswith('add'):
        addx,addReg = line.split()
        cycle += 1
        signal += signal_strength(cycle, reg)
        cycle += 1
        signal += signal_strength(cycle, reg)
        reg += int(addReg)
    
print(cycle, reg, signal)