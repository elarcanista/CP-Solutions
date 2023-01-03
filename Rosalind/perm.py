import itertools as iter

N = int(input())
print(len(list(iter.permutations(range(1, N+1)))))
for p in iter.permutations(range(1, N+1)):
    print(*p)