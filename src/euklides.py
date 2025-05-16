def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return abs(a * b) // nwd(a, b)


if __name__ == "__main__":
    x = 48
    y = 18
    print(f"NWD({x}, {y}) = {nwd(x, y)}")
    print(f"NWW({x}, {y}) = {nww(x, y)}")