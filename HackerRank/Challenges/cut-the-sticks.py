N = int(input())
L = list(map(int, input().split()))
while len(L) > 0:
    print(len(L))
    L2 = []
    m = min(L)
    for l in L:
        if l - m > 0:
            L2.append(l - m)
    L = L2