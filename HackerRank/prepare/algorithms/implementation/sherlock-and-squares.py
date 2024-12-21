# https://www.hackerrank.com/challenges/sherlock-and-squares/
import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    n = math.ceil(a**(1/2))
    ans = 0
    while n**2 <= b:
        ans += 1
        n += 1
    print(ans)
