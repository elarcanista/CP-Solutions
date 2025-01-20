# https://www.hackerrank.com/challenges/quicksort4/
def quicksort_inplace(arr, l, r):
    count = 0
    if r - l <= 1:
        return count
    pivot = arr[r - 1]
    mid = l
    for i in range(l, r - 1):
        if arr[i] < pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1
            count += 1
    arr[mid], arr[r - 1] = pivot, arr[mid]
    count += quicksort_inplace(arr, l, mid)
    count += quicksort_inplace(arr, mid + 1, r)
    return count + 1

def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        item = arr[i]
        j = i
        while j > 0 and arr[j - 1] >= item:
            count += 1
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item
    return count

input()
arr = list(map(int, input().split()))
print(insertion_sort(arr.copy()) - quicksort_inplace(arr, 0, len(arr)))
