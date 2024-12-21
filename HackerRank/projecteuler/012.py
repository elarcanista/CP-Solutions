# https://www.hackerrank.com/contests/projecteuler/challenges/euler012/
def num_divs(N, primes):
    if N <= 1:
        return 1
    N2 = N
    ans = 1
    i = 0
    p = 2
    prime = True
    while p*p <= N:
        n = 1
        while N2%p == 0:
            if p > primes[-1]:
                primes.append(p)
            prime = False
            N2 /= p
            n += 1
        ans *= n
        if p + 1 < primes[-1]:
            p = primes[i+1]
        else:
            p += 1
        i += 1
    if prime or N2 > 1:
        ans *= 2
    return ans

primes = [2]

def find(N, primes):
    i = 1
    k = i//2
    while num_divs(2*k+1, primes) * num_divs(k + i%2, primes) <= N:
        i += 1
        k = i//2
    return i*(i+1)//2

for _ in range(int(input())):
    N = int(input())
    print(find(N, primes))
