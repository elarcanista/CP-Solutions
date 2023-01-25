for _ in range(int(input())):
    input()
    N = list(map(int, input().split()))
    odd = 0
    even = 0
    for n in N:
        odd += 1 if n%2 == 1 else 0
        even += 1 if n%2 == 0 else 0
    ans = []
    if odd >= 3:
        odd = 3
        for i in range(len(N)):
            if odd != 0 and N[i] % 2 == 1:
                ans.append(i+1)
                odd -= 1
    elif odd >= 1 and even >= 2:
        even = 2
        odd = 1
        for i in range(len(N)):
            if even != 0 and N[i] % 2 == 0:
                ans.append(i+1)
                even -= 1
            if odd != 0 and N[i] % 2 == 1:
                ans.append(i+1)
                odd -= 1
    if len(ans) == 3:
        print("YES")
        print(*ans)
    else:
        print("NO")