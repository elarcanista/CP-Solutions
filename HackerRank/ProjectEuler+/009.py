#!/bin/python3

import sys

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    m = 1
    ans = []
    while m**2 <= N/2:
        if (N/2) % m == 0:
            k = m + 1 if m % 2 == 0 else m + 2
        else:
            m += 1
            continue
        while k <= (N/2)/m and k < 2*m:
            d = (N/2)/(m * k)
            n = k-m
            a = d * (m**2 - n**2)
            b = d * (2*m*n)
            c = d * (m**2 + n**2)
            if d == int(d) and a > 0 and b > 0 and c > 0:
                ans.append(a*b*c)
            k += 2
        m += 1
    if len(ans) == 0:
        print(-1)
    else:
        print(int(max(ans)))
