def add(S, n):
    i = len(S)
    S.append(n)
    while i > 1 and n > S[i//2]:
        S[i], S[i//2] = S[i//2], S[i]
        i //= 2

def sort(S):
    def sift(i):
        def left(i): return S[2*i] if 2*i <= last else None
        def right(i): return S[2*i + 1] if 2*i + 1 <= last else None

        while ((left(i) is not None and S[i] < left(i)) or
               (right(i) is not None and S[i] < right(i))):
            if right(i) is not None and left(i) < right(i):
                S[i], S[2*i + 1] = S[2*i + 1], S[i]
                i = 2*i + 1
                continue
            S[i], S[2*i] = S[2*i], S[i]
            i = 2*i

    last = len(S) - 1    
    while last >= 1:
        S[1], S[last] = S[last], S[1]
        last -= 1
        i = 1
        sift(i)
    return S


N = int(input())
S = list(map(int, input().split()))
ans = [None]
for s in S:
    add(ans, s)
print(*sort(ans)[1:])