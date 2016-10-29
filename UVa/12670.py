import sys
import math

def length(n):
    ans = 0
    while n>0:
        n = n >> 1
        ans += 1
    return ans-1

def msb(n):
    ans = 0
    while n>0:
        ans = n
        n -= (n & -n)
    return ans

def acum(n):
    n = int(n)
    if n <= 1:
        #print(n)
        return n
    lastPow = msb(n)
    #print(n,lastPow)
    if lastPow == n:
        ans = int(n//2*length(n)+1)
        #print(ans)
        return ans
    ans = int(acum(lastPow)+n-lastPow+acum(n-lastPow))
    #print(ans)
    return ans

while True:
    try:
        line = input()
    except EOFError:
        break
    tokens = line.strip().split(" ")
    a = int(tokens[0])
    b = int(tokens[1])
    a = acum(a-1)
    b = acum(b)
    #print(a,)
    #print(b)
    print(b-a)
