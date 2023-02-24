NA = int(input())
A = sorted(list(map(int, input().split()))) + [None]
NB = int(input())
B = sorted(list(map(int, input().split()))) + [None]

missing = []
i = j = 0
last = None
while i <= NA and j <= NB:
    if last == B[j]:
        j += 1
        continue
    if A[i] != B[j]:
        missing.append(B[j])
        last = B[j]
        j += 1
    else:
        i += 1
        j += 1

print(*missing)