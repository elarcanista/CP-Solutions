K, N = map(int, input().split())
for _ in range(K):
    S = list(map(int, input().split()))
    sums = {}
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] + S[j] not in sums:
                sums[S[i] + S[j]] = (i+1, j+1)
    for i in range(len(S)):
        if -S[i] in sums and i+1 > max(sums[-S[i]]):
            print(*sums[-S[i]], i+1)
            break
    else:
        print(-1)