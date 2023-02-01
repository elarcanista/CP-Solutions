for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    for i in range(len(S) - 1):
        if S[i] == -1 and S[i+1] == -1:
            print(sum(S) + 4)
            break
    else:
        if -1 in S:
            print(sum(S))
        else:
            print(sum(S) - 4 )