N = int(input())
N = list(map(int, input().split()))
M = int(input())
M = list(map(int, input().split()))
K = []
i = 0
j = 0
while i < len(N) and j < len(M):
    if N[i] < M[j]:
        K.append(N[i])
        i += 1
    else:
        K.append(M[j])
        j += 1
if i == len(N):
    while j < len(M):
        K.append(M[j])
        j += 1
else:
    while i < len(N):
        K.append(N[i])
        i += 1
print(*K)