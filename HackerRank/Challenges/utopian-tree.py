for _ in range(int(input())):
    N = int(input())
    ans = 1
    for n in range(N):
        if n % 2 == 0:
            ans *= 2
        else:
            ans += 1
    print(ans)