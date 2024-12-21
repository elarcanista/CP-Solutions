# https://www.hackerrank.com/challenges/30-running-time-and-complexity/
import sys
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**(1/2))+1, 2):
        if n % i == 0:
            return False
    return True
    
N = int(input().strip())
for i in range(N):
    num = int(input().strip())
    prime = isPrime(num)
    if prime:
        print("Prime")
    else:
        print("Not prime")
