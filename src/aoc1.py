def change_direction(current_direction, turn):
    if turn == 'L':
        return (current_direction - 1) % 4
    else:
        return (current_direction + 1) % 4

def move(position, direction, distance):
    x, y = position
    if direction == 0:  # North
        return x, y + distance
    elif direction == 1:  # East
        return x + distance, y
    elif direction == 2:  # South
        return x, y - distance
    elif direction == 3:  # West
        return x - distance, y

def apply_instruction(position, direction, instruction):
    turn = instruction[0]
    distance = int(instruction[1:])
    new_direction = change_direction(direction, turn)
    new_position = move(position, new_direction, distance)
    return new_position, new_direction

def apply_instructions(instructions):
    position = (0, 0)
    direction = 0  # 0-North, 1-East, 2-South, 3-West
    for instruction in instructions:
        position, direction = apply_instruction(position, direction, instruction)
    return position

text = "L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1"
instructions = [instr.strip() for instr in text.split(',')]
final_position = apply_instructions(instructions)
distance_from_start = abs(final_position[0]) + abs(final_position[1])
print("Distance:", distance_from_start)
