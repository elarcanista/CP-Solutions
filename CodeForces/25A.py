N = int(input())
S = list(map(int, input().split()))
even = 0
odd = 0
for s in S:
    if s % 2 == 0:
        even += 1
    else:
        odd += 1

if even < odd:
    for i, s in enumerate(S):
        if s % 2 == 0:
            print(i + 1)
            break
else:
    for i, s in enumerate(S):
        if s % 2 == 1:
            print(i + 1)
            break