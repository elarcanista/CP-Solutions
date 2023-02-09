S, N = map(int, input().split())
d = []
for _ in range(N):
    d.append(tuple(map(int, input().split())))
d = sorted(d)
for s, b in d:
    if S <= s:
        print("NO")
        break
    S += b
else:
    print("YES")