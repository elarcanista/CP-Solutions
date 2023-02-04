for _ in range(int(input())):
    N, C = map(int, input().split())
    costs = list(range(1, N+1))
    for i, c in enumerate(map(int, input().split())):
        costs[i] += c
    ans = 0
    for c in sorted(costs):
        if C >= c:
            ans += 1
            C -= c
        else:
            break
    print(ans)