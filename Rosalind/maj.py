N, K = map(int, input().split())
ans = []
for _ in range(N):
    arr = list(map(int, input().split()))
    arr_unique = {}
    for a in arr:
        if a not in arr_unique:
            arr_unique[a] = 0
        arr_unique[a] += 1
        if arr_unique[a] > len(arr) // 2:
            ans.append(a)
            break
    else:
        ans.append(-1)
print(*ans)