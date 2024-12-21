# https://www.hackerrank.com/challenges/happy-ladybugs/
from collections import Counter
from itertools import groupby

for _ in range(int(input())):
    N = int(input())
    S = input()
    C = Counter(S)
    if "_" in C:
        C.pop("_")
        if all(v > 1 for v in C.values()):
            print("YES")
        else:
            print("NO")
    else:
        if all(len(list(l)) > 1 for _, l in groupby(S)):
            print("YES")
        else:
            print("NO")
