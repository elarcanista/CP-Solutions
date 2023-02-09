N = int(input())
S = map(int, input().split())
min_S = next(S)
max_S = min_S

ans_min = 0
ans_max = 0
for s in S:
    if s < min_S:
        min_S = s
        ans_min += 1
    if s > max_S:
        max_S = s
        ans_max += 1

print(ans_max, ans_min)