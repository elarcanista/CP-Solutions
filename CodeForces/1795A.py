for _ in range(int(input())):
    A, B = map(int, input().split())
    A = input()
    B = input()
    C = A + B[::-1]
    last = None
    ans = 0
    for c in C:
        if c == last:
            ans += 1
        last = c
    if ans <= 1:
        print("YES")
    else:
        print("NO")