# https://www.hackerrank.com/challenges/quicksort2/
def partition(arr):
    if len(arr) <= 1:
        return arr
    left = []
    mid = []
    right = []
    pivot = arr[0]
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            mid.append(item)
        else:
            right.append(item)
    ans = partition(left) + mid + partition(right)
    print(" ".join(map(str, ans)))
    return ans

_ = input()
arr = list(map(int, input().split()))
partition(arr)
