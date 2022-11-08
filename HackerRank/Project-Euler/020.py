def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

for _ in range(int(input())):
    N = int(input())
    print(sum(map(int, list(str(factorial(N))))))