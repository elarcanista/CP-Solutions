from math import *
N = int(input())

digits = [i**N for i in range(10)]

d = 1
mid = log10(d) + N*log10(9) + 1
while not (d <= mid and mid <= d+1):
    d += 1
    mid = log10(d) + N*log10(9) + 1
ans = 0

for n in range(2, int(10**(d-0.5))):
    if n == sum(map(lambda x: digits[int(x)], list(str(n)))):
        ans += n
print(ans)