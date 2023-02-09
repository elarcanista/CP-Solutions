#!/bin/python3

import sys

n = int(input().strip())
temp = 1
for i in range(n):
    temp *= (i+1)
print(temp)