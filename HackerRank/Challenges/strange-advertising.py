N = int(input())
curr = 5
ans = 0
for n in range(N):
    likes = curr // 2
    curr = likes * 3
    ans += likes
print(ans)