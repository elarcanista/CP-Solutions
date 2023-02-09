N, M = map(int, input().split())
NS = list(map(int, input().split()))
MS = list(map(int, input().split()))

ans = 0
for i in range(max(NS), min(MS)+1):
    if all(map(lambda x: i%x == 0, NS)) and all(map(lambda x: x%i == 0, MS)):
        ans += 1
print(ans)