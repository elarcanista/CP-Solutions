# https://www.hackerrank.com/contests/projecteuler/challenges/euler040/

def series(N, r):
    r_exp = r ** (N + 1)
    geom = (r_exp - 1) // (r - 1)
    left = r_exp * (N + 1)
    right = r * geom
    arith_geom = (left - right) // (r - 1)
    return arith_geom + geom

def search(k, digit):
    while digit > 9 * series(k + 1, 10):
        k += 1
    lower = 9 * series(k, 10) + 1
    upper = 9 * series(k + 1, 10) + 1
    k += 1
    digit -= lower
    upper -= lower
    curr = 10 ** k + digit // (k + 1)
    mod = digit % (k + 1)
    return str(curr)[mod], k - 1

for _ in range(int(input())):
    digits = sorted(map(int, input().split()))
    ans = 1
    k = -1
    for d in digits:
        D, k = search(k, d)
        ans *= int(D)
    print(ans)
