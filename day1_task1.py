# Original solution for part 1 of day 1

dial = 50
code = 0

with open("day1.txt", "r") as f:
    for n in f.readlines():
        if n.startswith("R"):
            x = int(n[1:].strip())
            dial += x
            if dial % 100 == 0:
                code += 1
        elif n.startswith("L"):
            x = int(n[1:].strip())
            dial -= x
            if dial % 100 == 0:
                code += 1

print(code)