matches = ""
points = 0

with open("day2.txt", "r") as f:
    for i in f:
        matches += i
matches = matches.split("\n")
print(matches)

for i in matches:
    n = i.split(" ")
    match n[0]:
        case "A": #rock
            match n[1]:
                case "X": #rock - 1
                    points += 4
                case "Y": #paper - 2
                    points += 8
                case "Z": #scissors - 3
                    points += 3

        case "B": #paper
            match n[1]:
                case "X": #rock - 1
                    points += 1
                case "Y": #paper - 2
                    points += 5
                case "Z": #scissors - 3
                    points += 9

        case "C": #scissor
            match n[1]:
                case "X": #rock - 1
                    points += 7
                case "Y": #paper - 2
                    points += 2
                case "Z": #scissors - 3
                    points += 6

print(points)

#part 2
points = 0

for i in matches:
    n = i.split(" ")
    match n[0]:
        case "A": #rock
            match n[1]:
                case "X": #lose - scissors - 3
                    points += 3
                case "Y": #draw - rock - 1
                    points += 4
                case "Z": #win - paper - 2
                    points += 8

        case "B": #paper
            match n[1]:
                case "X": #lose - rock - 1
                    points += 1
                case "Y": #draw - paper - 2
                    points += 5
                case "Z": #win - scissors - 3
                    points += 9

        case "C": #scissor
            match n[1]:
                case "X": #lose - paper - 2
                    points += 2
                case "Y": #draw - scissor - 3
                    points += 6
                case "Z": #win - rock - 1
                    points += 7

print(points)