# https://www.hackerrank.com/challenges/kangaroo/
x1, v1, x2, v2 = map(int, input().split())
if v1 < v2:
    x1, x2 = x2, x1
    v1, v2 = v2, v1
if v1 == v2:
    if  x1 != x2:
        print("NO")
    else:
        print("YES")
else:
    while x1 < x2:
        x1 += v1
        x2 += v2
    if  x1 != x2:
        print("NO")
    else:
        print("YES")
