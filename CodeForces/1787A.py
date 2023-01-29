for _ in range(int(input())):
    N = int(input())
    if N%2 == 0:
        print(1, N//2)
    else:
        print(-1)