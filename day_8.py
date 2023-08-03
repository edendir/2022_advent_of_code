import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "day8.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

GRID = []
for line in lines:
    row = line
    GRID.append(row)

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ROWS = len(GRID)
COLUMNS = len(GRID[0])

part1 = 0
for row in range(ROWS):
    for column in range(COLUMNS):
        visible = False
        for (dr, dc) in DIRECTIONS:
            rr = row
            cc = column
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<ROWS and 0<=cc<COLUMNS):
                    break
                if GRID[rr][cc] >= GRID[row][column]:
                    ok = False
            if ok:
                visible = True
        if visible:
            part1 += 1
print(part1)

part2 = 0
for row in range(ROWS):
    for column in range(COLUMNS):
        score = 1
        for (dr, dc) in DIRECTIONS:
            dist = 1
            rr = row + dr
            cc = column + dc
            while True:
                if not (0<=rr<ROWS and 0<=cc<COLUMNS):
                    dist -= 1
                    break
                if GRID[rr][cc] >= GRID[row][column]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        part2 = max(part2, score)
print(part2)