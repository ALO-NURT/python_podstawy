x=0
y=0
dir="n"

def turn_direction(dir, turn):
    dirs = ["n", "e", "s", "w"]
    i = dirs.index(dir)
    if turn == "L":
        i = (i - 1) % 4
    else:  # turn == "R"
        i = (i + 1) % 4
    return dirs[i]

instr = """R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3,
R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2,
R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4,
R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4,
R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5,
L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5,
L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1,
R3, L5, R1, R4"""

steps = [s.strip() for s in instr.split(",")]
d=0
y= 0
x = 0

for s in steps:
    turn =s[0]
    dist = int(s[1:])

    if turn == "R":
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

    if d ==0:
        y += dist
    elif d == 1:
        x += dist
    elif d ==2:
        y -= dist
    else:
        x -= dist

print("odleglosc od srodka:", abs(x) + abs(y))

