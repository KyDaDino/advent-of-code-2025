# Original solution for part 2 of day 1

dial = 50
code = 0

with open("day1.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("R"):
            x = int(line[1:].strip())
            for _ in range(x-1):
                dial += 1
                if dial % 100 == 0:
                    code += 1
            dial += 1
            if dial % 100 == 0:
                code += 1
        elif line.startswith("L"):
            x = int(line[1:].strip())
            for _ in range(x-1):
                dial -= 1
                if dial % 100 == 0:
                    code += 1
            dial -= 1
            if dial % 100 == 0:
                code += 1

print(code)