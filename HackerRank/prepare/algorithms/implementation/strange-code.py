# https://www.hackerrank.com/challenges/strange-code/
import math

N = int(input())
layer = lambda N : math.ceil(math.log2(N/3 + 1) - 1)
dist = lambda N: N - 3*(2**(layer(N)) - 1) - 1
init = lambda N: 3*2**layer(N)
ans = lambda N: init(N) - dist(N)

print(ans(N))
