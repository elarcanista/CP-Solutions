N = int(input())
L = list(map(int, input().split()))
curr = 0
ans = 0
while curr != N - 1:
    if curr + 2 < N and L[curr + 2] == 0:
        curr += 1
    curr += 1
    ans += 1
print(ans)