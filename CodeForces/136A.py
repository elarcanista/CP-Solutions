N = int(input())
S = list(map(int, input().split()))
T = [0] * N
for i, s in enumerate(S):
    T[s-1] = i+1
print(*T)