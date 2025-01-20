# https://www.hackerrank.com/challenges/quicksort3/
def quicksort_inplace(arr, l, r):
    if r - l <= 1:
        return
    pivot = arr[r - 1]
    mid = l
    for i in range(l, r - 1):
        if arr[i] < pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1
    arr[mid], arr[r - 1] = pivot, arr[mid]
    print(" ".join(map(str, arr)))
    quicksort_inplace(arr, l, mid)
    quicksort_inplace(arr, mid + 1, r)

input()
arr = list(map(int, input().split()))
quicksort_inplace(arr, 0, len(arr))
