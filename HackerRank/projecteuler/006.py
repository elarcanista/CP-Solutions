# https://www.hackerrank.com/contests/projecteuler/challenges/euler006/
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = n*(n+1)/2
    i2 = (n**3)/3+(n**2)/2+n/6
    print(int(abs(i2-i*i)))
