import itertools as iter

letters = sorted(input().split())
n = int(input())
for perm in iter.product(letters, repeat=n):
    print("".join(perm))

