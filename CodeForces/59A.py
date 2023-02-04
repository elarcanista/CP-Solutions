S = input()
lower = 0
upper = 0
for c in S:
    if c.lower() == c:
        lower += 1
    else:
        upper += 1
if lower >= upper:
    print(S.lower())
else:
    print(S.upper())