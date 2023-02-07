N = int(input())
ans = "I hate"
for n in range(1, N):
    if n%2 == 1:
        ans += " that I love"
    else:
        ans += " that I hate"
ans += " it"
print(ans)