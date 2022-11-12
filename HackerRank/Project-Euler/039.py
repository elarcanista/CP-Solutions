def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def fill(S_max):
    S = [0] * (S_max + 1)
    m = 2
    while 2 * m**2 <= S_max:
        n = 1 + (m % 2 != 0)
        while n <= m:
            if gcd(m, n) == 1:
                k = 1
                s = 2 * k * m * (m + n)
                while s <= S_max:
                    S[s] += 1
                    k += 1
                    s = 2 * k * m * (m + n)
            n += 1 + (m % 2 != 0)
        m += 1
    return S

def cum_max(S):
    S_max = [0] * len(S)
    for i in range(1, len(S)):
        if S[i] > S[S_max[i-1]]:
            S_max[i] = i
        else:
            S_max[i] = S_max[i-1]
    return S_max

max_N = 5 * 10**6
S = fill(max_N)
S_max = cum_max(S)

for _ in range(int(input())):
    N = int(input())
    print(S_max[N])
