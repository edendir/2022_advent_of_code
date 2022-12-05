with open("day4.txt") as f:
    text = f.read().strip()
    lines = text.split('\n')

def part1():
    s = 0
    for l in lines:
        s1, e1, s2, e2 = (*(int(a) for a in l.split(',')[0].split('-')), *(int(a) for a in l.split(',')[1].split('-')))
        if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
            s += 1
    return s


def part2():
    count = 0
    for line in lines:
        l1, l2 = line.split(",")
        (min1, max1), (min2, max2) = l1.split("-"), l2.split("-")
        min1, max1, min2, max2 = list(map(int, [min1, max1, min2, max2]))
        if (min1 <= min2 <= max1) or (min2 <= min1 <= max2):
            count += 1
    return count


print(part1())
print(part2())
