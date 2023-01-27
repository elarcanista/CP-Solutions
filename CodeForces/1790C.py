for _ in range(int(input())):
    S = []
    for _ in range(int(input())):
        S.append(list(map(int, input().split())))
    ans = []
    while len(ans) < len(S):
        freq = {}
        for s in S:
            if len(s) > 0:
                if s[0] not in freq:
                    freq[s[0]] = 0
                else:
                    ans.append(s[0])
                    break
        for i in range(len(S)):
            if len(S[i]) > 0 and S[i][0] == ans[-1]:
                S[i] = S[i][1:]
    print(*ans)