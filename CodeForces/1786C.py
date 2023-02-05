for _ in range(int(input())):
    N = int(input())
    S = sorted(list(map(int, input().split())))
    ans = 0
    last = 0
    for s in S:
        if s > last:
            last += 1
            ans += s - last
    print(ans)
