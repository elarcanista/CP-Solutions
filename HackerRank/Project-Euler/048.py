import math

mod = 10**10
ans = 0
for i in range(1, 11):
    ans += math.pow(i,i, mod)
print(ans % mod)