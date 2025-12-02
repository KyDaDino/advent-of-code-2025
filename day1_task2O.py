# Optimised solution for task 2 of day 1

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