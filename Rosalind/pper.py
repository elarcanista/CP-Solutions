n, k = map(int, input().split())

def pperm(N, K):
    ans = 1
    for k in range(K):
        ans *= max(1, N-k)
    return ans

print(pperm(n, k) % 10**6)