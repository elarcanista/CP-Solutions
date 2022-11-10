fact = [1] * 10
for n in range(1, len(fact)):
    fact[n] = fact[n-1] * n

N = int(input())

ans = 0
for n in range(10, N):
    f = sum(map(lambda x: fact[int(x)], str(n)))
    if f % n == 0:
        ans += n
print(ans)