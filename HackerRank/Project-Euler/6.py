#!/bin/python3
#Project Euler #6 - Sum square difference

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = n*(n+1)/2
    i2 = (n**3)/3+(n**2)/2+n/6
    print(int(abs(i2-i*i)))
