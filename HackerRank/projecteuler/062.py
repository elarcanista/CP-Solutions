# https://www.hackerrank.com/contests/projecteuler/challenges/euler062/
cubes = {}
keys = set()
values = []

N, K = map(int, input().split())
for n in range(1, N):
    c = n**3
    c = "".join(sorted(str(c)))
    if c in cubes:
        cubes[c][0] += 1
        cubes[c][1].append(n)
    else:
        cubes[c] = [1, [n]]
    if cubes[c][0] == K:
        keys.add(c)
    if cubes[c][0] > K:
        keys.discard(c)

for c in keys:
    values.append(cubes[c][1][0])

for c in sorted(values):
    print(c**3)
