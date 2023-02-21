N = int(input())
M2 = []
for _ in range(N):
    M2.append(list(input()))
M = [list(map(int, row)) for row in M2]

for r in range(1, len(M)-1):
    for c in range(1, len(M)-1):
        if all(map(lambda x: x < M[r][c], 
               [M[r-1][c], M[r][c+1], M[r+1][c], M[r][c-1]])):
            M2[r][c] = "X"
for row in M2:
    print("".join(row))