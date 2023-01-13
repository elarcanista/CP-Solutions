import sys

E = int(input())
V = 0

for line in sys.stdin:
    V += 1

print(E-1-V)