N, K, Q = map(int, input().split())
L = list(map(int, input().split()))
for _ in range(Q):
    q = int(input())
    print(L[(q - K) % N])