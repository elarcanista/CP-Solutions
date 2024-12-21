# https://www.hackerrank.com/challenges/encryption/
import math
S = input()
C = math.ceil(len(S) ** (1/2))
R = math.ceil(len(S) / C)
M = []
for r in range(R):
    M.append(S[r*C: r*C + R + 1])

M[-1] += (" " * (C - len(M[-1])))

ans = []
for c in range(C):
    ans.append("".join([r[c] for r in M]).strip())
    
print(*ans)
