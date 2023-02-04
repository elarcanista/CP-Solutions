N = int(input())
S = input()
ans = 0
last = ""
for c in S:
    if c == last:
        ans += 1
    last = c
print(ans)