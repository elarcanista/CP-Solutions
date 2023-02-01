for i in range(5):
    line = list(map(int, input().split()))
    if 1 in line:
        r = i
        c = line.index(1)
print(abs(r-2) + abs(c-2))