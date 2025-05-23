def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(nwd(48, 18))

import math

def nww(a, b):
    return abs(a * b) // math.gcd(a, b)

print(nww(12, 18))