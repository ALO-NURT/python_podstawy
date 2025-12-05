instr = """R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1,
 L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5,
 L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2,
 R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3,
 L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4,
 L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4,
 L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2,
 R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3,
 R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1,
 L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"""

steps = [s.strip() for s in instr.split(",")]

d = 0
x = 0
y = 0

for s in steps:
    turn = s[0]
    dist = int(s[1:])

    if turn == "R":
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

    if d == 0:
        y += dist
    elif d == 1:
        x += dist
    elif d == 2:
        y -= dist
    else:
        x -= dist

print("Wraz końcowy:", x, y)
print("Odległość od środka:", abs(x) + abs(y))