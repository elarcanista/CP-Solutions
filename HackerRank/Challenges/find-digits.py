for _ in range(int(input())):
    N = input()
    ans = 0
    for c in N:
        if c != "0" and int(N) % int(c) == 0:
            ans += 1
    print(ans)