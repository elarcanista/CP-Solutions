b, n, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))

max = -1
for n in N:
    for m in M:
        if n + m <= b and n + m > max:
            max = n + m
print(max)