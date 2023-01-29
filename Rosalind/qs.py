def sort(S):
    if len(S) <= 1:
        return S
    pivot = S.pop()
    L = []
    M = []
    R = []
    for s in S:
        if s < pivot:
            L.append(s)
        if s > pivot:
            R.append(s)
        if s == pivot:
            M.append(s)
    L = sort(L)
    R = sort(R)
    return L + M + [pivot] + R

N = int(input())
S = list(map(int, input().split()))
print(*sort(S))