# https://www.hackerrank.com/challenges/organizing-containers-of-balls/
for _ in range(int(input())):
    M = []
    for _ in range(int(input())):
        M.append(list(map(int, input().split())))
    sum_cols = []
    for c in range(len(M[0])):
        sum_cols.append(sum([r[c] for r in M]))
    sum_rows = []
    for r in M:
        sum_rows.append(sum(r))
    if sorted(sum_cols) == sorted(sum_rows):
        print("Possible")
    else:
        print("Impossible")
