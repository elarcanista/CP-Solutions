def ranking(p):
    l = 0
    r = len(ranked)
    while (l < r):
        mid = (l + r) // 2
        if ranked[mid] > p:
            r = mid
        else:
            l = mid + 1
    return r - 1

N = int(input())
ranked = sorted(list(set(map(int, input().split()))))
M = int(input())
player = list(map(int, input().split()))
for p in player:
    print(len(ranked) - ranking(p))