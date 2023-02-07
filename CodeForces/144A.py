N = int(input())
S = list(map(int, input().split()))
M = max(S)
m = min(S)

for M_i, s in enumerate(S):
    if s == M:
        break

for m_i, s in reversed(list(enumerate(S))):
    if s == m:
        break

ans = M_i
if M_i > m_i:
    ans -= 1
ans += len(S) - m_i - 1
print(ans)