for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    neg = 0
    for s in S:
        if s < 0:
            neg += 1
    ans = sum(map(abs, S))
    if neg % 2 == 1:
        ans -= 2*min(map(abs, S))
    print(ans)