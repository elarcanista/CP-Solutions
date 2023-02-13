N, K = map(int, input().split())
L = list(map(int, input().split()))
last = None
i = 0
ans = 100
while last != 0:
    i = (i + K) % N
    ans -= 1
    if L[i] == 1:
        ans -= 2
    last = i
print(ans)