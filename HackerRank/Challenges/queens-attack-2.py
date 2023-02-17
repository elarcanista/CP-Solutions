import itertools as iter

size, N = map(int, input().split())
Q = complex(*map(int, input().split()))
obstacles = set()
for _ in range(N):
    obstacles.add(complex(*map(int, input().split())))
moves = map(lambda x: complex(*x), iter.product([-1, 0 , 1], repeat=2))
ans = 0
for m in moves:
    if m == 0:
        continue
    curr = Q
    boundaries = True
    while boundaries and curr not in obstacles:
        ans += 1
        curr += m
        boundaries = curr.real >= 1 and curr.real <= size and curr.imag >= 1 and curr.imag <= size
    else:
        ans -= 1
print(ans)