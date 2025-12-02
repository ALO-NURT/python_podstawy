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
