import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "day10.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

G = [['?' for _ in range(40)] for _ in range(6)]
cycle = 0
reg = 1
signal = 0

def signal_strength(cycle, x):
    global signal
    global G
    cycle1 = cycle - 1
    G[cycle1//40][cycle1%40] = ('#' if abs(x-(cycle1%40))<=1 else '.')
    if cycle in (20, 60, 100, 140, 180, 220):
        signal += cycle*x
    
    
for line in lines:
    if line.startswith('noop'):
        signal_strength(cycle, reg)
        cycle += 1
    elif line.startswith('add'):
        addx,addReg = line.split()
        signal_strength(cycle, reg)
        cycle += 1
        signal_strength(cycle, reg)
        cycle += 1
        reg += int(addReg)
    
print(cycle, reg, signal)
for r in range(6):
    print(''.join(G[r]))