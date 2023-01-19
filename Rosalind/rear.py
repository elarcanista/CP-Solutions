import sys

def reversal(A, i, j):
    ss = A[i: j]
    return A[:i] + ss[::-1] + A[j:]

def get_breaks(A, B):
    ans = []
    for i in range(len(B)-1):
        if abs(A.index(B[i+1]) - A.index(B[i])) > 1:
            ans.append(i + 1)
    return ans

def get_best(A, Bs):
    revs = []
    for B in Bs:
        breaks = get_breaks(A, B)
        for i in range(len(breaks) - 1):
            for j in range(i + 1, len(breaks)):
                b = reversal(B, breaks[i], breaks[j])
                revs.append(b)
    min_breaks = len(A)
    min_revs = []
    for r in revs:
        breaks = len(get_breaks(A, r))
        if breaks < min_breaks:
            min_breaks = breaks
            min_revs = [r]
        elif breaks == min_breaks:
            min_revs.append(r)
    return min_revs

def dist(A, B):
    B = tuple([0] + B + [len(B) + 1])
    moves = 0
    curr = [B]
    A = tuple([0] + A + [len(A) + 1])
    while A not in curr:
        curr = get_best(A, curr)
        moves += 1
    return moves

for i, line in enumerate(sys.stdin):
    if i % 3 == 0:
        A = list(map(int, line.strip().split()))
    if i % 3 == 1:
        B = list(map(int, line.strip().split()))
        print(dist(A, B))
