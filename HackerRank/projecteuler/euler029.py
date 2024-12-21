# https://www.hackerrank.com/contests/projecteuler/challenges/euler029/
N = int(input())

# x = (y^a)^b
max_a = 16
min_a = [0] * ((N + 1) * max_a)
for a in range(1, max_a + 1):
    for b in range(1, N + 1):
        if min_a[a*b] == 0:
            min_a[a*b] = a

base = [0] * (N + 1)
repeated = 0
for x in range(2, N+1):
    if base[x] == 0:
        b = 2
        yab = x**2
        while yab <= N:
            base[yab] = (x, b)
            yab *= x
            b += 1
    else:
        y, a = base[x]
        for b in range(2, N+1):
            if min_a[a*b] < a:
                repeated += 1

print((N - 1)**2 - repeated)
