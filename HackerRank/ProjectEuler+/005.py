#!/bin/python3
#HackerRank Project Euler#5 - Smallest multiple

import sys
import math

primes = [2, 3]
for i in range(5, 40, 2):
    prime = True
    for j in primes:
        if i % j == 0:
            prime = False
            break
    if prime:
        primes.append(i)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp = 1
    for i in primes:
        if i > n:
            break
        temp2 = i**int(math.log(n,i))
        temp *= temp2
    print(temp)
