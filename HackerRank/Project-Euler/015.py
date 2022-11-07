def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def choose(m, n):
    ans = 1
    for i in range(n+1, m+1):
        ans *= i
    return ans//fact(m-n)

for _ in range(int(input())):
    m, n = map(int, input().split())
    print(choose(m + n, m))