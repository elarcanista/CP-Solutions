K, N = map(int, input().split())

for _ in range(K):
    S = list(map(int, input().split()))
    values = {}
    for i in range(len(S)):
        if -S[i] in values:
            print(values[-S[i]] + 1, i + 1)
            break
        if S[i] not in values:
            values[S[i]] = i
    else:
        print(-1)