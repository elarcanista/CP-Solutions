curr = 0
ans = 0
for _ in range(int(input())):
    p_out, p_in = map(int, input().split())
    curr += p_in - p_out
    ans = max(curr, ans)
print(ans)