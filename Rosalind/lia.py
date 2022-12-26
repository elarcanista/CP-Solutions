def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def choose(n, k):
    return fact(n)/(fact(k)*(fact(n-k)))

def P(n):
    return choose(2**k, n) * ((1/4)**n) * ((3/4)**(2**k - n))

k, N = map(int, input().split())

ans = 1
for n in range(N):
    ans -= P(n)
print(ans)