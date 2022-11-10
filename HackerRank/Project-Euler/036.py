def palindrome(N):
    N = str(N)
    for i in range(len(N)//2):
        if N[i] != N[-i-1]:
            return False
    return True

def to_base(N, b):
    n = 0
    pwr = 1
    while N != 0:
        n += (N % b) * pwr
        N = N//b
        pwr *= 10
    return n

N, b = map(int, input().split())

ans = 0 
for n in range(N+1):
    if palindrome(n) and palindrome(to_base(n, b)):
        ans += n
print(ans)