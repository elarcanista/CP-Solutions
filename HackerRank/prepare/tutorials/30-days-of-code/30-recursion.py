# https://www.hackerrank.com/challenges/30-recursion/
def factorial(N):
    if N <= 0:
        return 1
    return (N * factorial(N-1))
    
n = int(input())
print(factorial(n))

