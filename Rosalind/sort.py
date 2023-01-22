def get_breaks(A, B):
    ans = []
    for i in range(len(B) - 1):
        if abs(A.index(B[i]) - A.index(B[i+1])) > 1:
            ans.append(i+1)
    return ans

def rev(B, i, j):
    return B[:i] + B[i:j][::-1] + B[j:]

def get_best(A, curr):
    r = []
    for B, hist in curr:
        breaks = get_breaks(A, B)
        for i in range(len(breaks) - 1):
            for j in range(i + 1, len(breaks)):
                r.append((
                    rev(B, breaks[i], breaks[j]), 
                    hist + [(breaks[i], breaks[j])]))
    ans = []
    min_breaks = len(A)
    for B, hist in r:
        breaks = get_breaks(A, B)
        if len(breaks) < min_breaks:
            min_breaks = len(breaks)
            ans = [(B, hist)]
        elif len(breaks) == min_breaks:
            ans.append((B, hist))
    return ans

def dist(A, B):
    A = ["-"] + A + ["+"]
    B = ["-"] + B + ["+"]
    curr = [(B, [])]
    while A not in list(zip(*curr))[0]:
        curr = get_best(A, curr)
    return curr[0][1]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
hist = dist(B, A)
print(len(hist))
for i,j in hist:
    print(i, j-1)