A = list(map(float, input().split()))
B = list(map(float, input().split()))

max_mult = (0, 0)
for a in A:
    for b in B:
        dif = round(a-b, 5)
        C = list(map(lambda x: x + dif, B))
        D = [round(x - y, 5) for x in A for y in C]
        d = D.count(0)
        if max_mult[0] < d:
            max_mult = (d, dif)

print(*max_mult, sep="\n")