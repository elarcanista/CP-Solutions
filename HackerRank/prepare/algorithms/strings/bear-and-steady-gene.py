# https://www.hackerrank.com/challenges/bear-and-steady-gene/
from math import inf

def min_range(gene):
    proteins = "ACGT"
    balance = {c: -n // 4 for c in proteins}
    for c in gene:
        balance[c] += 1
    good = all(balance[c] == 0 for c in proteins)
    if good:
        return 0
    count = {c: 0 for c in proteins}
    start = end = 0
    ans = inf
    while end < len(gene):
        while end < len(gene) and not good:
            count[gene[end]] += 1
            good = all(count[c] >= balance[c] for c in proteins)
            end += 1
        if good:
            ans = min(ans, end - start)
        count[gene[start]] -= 1
        good = all(count[c] >= balance[c] for c in proteins)
        start += 1
    return ans

n = int(input())
gene = input()
print(min_range(gene))
