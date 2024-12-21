# https://www.hackerrank.com/challenges/30-bitwise-and/
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    maxi = 0
    i = n
    while i > maxi:
        j = min(i-1,k+1)
        while j > maxi:
            curr = i & j
            if curr > maxi and curr < k:
                maxi = curr
            j-=1
        i-=1
        
    print(maxi)
