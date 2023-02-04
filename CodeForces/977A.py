def substract(N, K):
    for _ in range(K):
        if N % 10 != 0:
            N -= 1
        else:
            N //= 10
    return N

N, K = map(int, input().split())
print(substract(N, K))