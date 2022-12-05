N = int(input())
m = 0
for a in range(1, N):
    for b in range(1, N):
        n = sum(map(int, list(str(a ** b))))
        if n > m:
            m = n
print(m)
