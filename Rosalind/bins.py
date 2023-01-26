def bs(q, arr):
    l = 0
    r = len(arr)
    while l <= r:
        m = (l + r) // 2
        if arr[m] == q:
            return m + 1
        elif arr[m] < q:
            l = m + 1
        else:
            r = m - 1
    return -1

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))
print(*[bs(q, arr) for q in query])