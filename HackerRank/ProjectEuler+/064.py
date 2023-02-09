fractional = {}

def try2(n):
    r = n**(1/2)
    a = int(r)
    b = 1
    c = a
    A = {}
    count = 0

    while (a, b, c) not in A:
        if a == r:
            return 0
        A[(a, b, c)] = count
        count += 1

        den = (n - c**2)
        r = (n**(1/2) + c) * (b/den)
        a = int(r)
        b = den // b
        c = a * b - c

    return count-1


N = int(input())

ans = 0
for n in range(N+1):
    if try2(n) % 2 != 0:
        ans += 1
print(ans)