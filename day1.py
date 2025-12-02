# Task 1

"""dial = 50
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

print(code)"""

# Task 2

"""dial = 50
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

print(code)"""

# Task 3 (Optimisations)

def checkzero(x):
    global code
    if x % 100 == 0:
        code += 1


dial = 50
code = 0

with open("day1.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("R"):
            x = int(line[1:].strip())
            for _ in range(x):
                dial += 1
                checkzero(dial)
        else:
            x = int(line[1:].strip())
            for _ in range(x):
                dial -= 1
                checkzero(dial)

print(code)