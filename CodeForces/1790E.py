for _ in range(int(input())):
    N = int(input())
    a = N // 2
    b = a * 3
    if a ^ b == N:
        print(a, b)
    else:
        print(-1)