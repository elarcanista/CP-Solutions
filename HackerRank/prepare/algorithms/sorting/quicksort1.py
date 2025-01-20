# https://www.hackerrank.com/challenges/quicksort1/
def partition(arr):
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
    return left + mid + right

_ = input()
arr = list(map(int, input().split()))
print(" ".join(map(str, partition(arr))))
