# https://www.hackerrank.com/challenges/larrys-array/
for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    inversions = 0
    for i, s in enumerate(S):
        for s2 in S[i+1:]:
            if s > s2:
                inversions += 1
    if inversions % 2 == 0:
        print("YES")
    else:
        print("NO")
