N = int(input())
ans = N//5
if N % 5 != 0:
    ans += 1
print(ans)
