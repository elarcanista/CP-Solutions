# https://www.hackerrank.com/challenges/insertionsort1/
def insert(arr):
    item = arr[-1]
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= item:
        arr[i] = arr[i - 1]
        print(" ".join(map(str, arr)))
        i -= 1
    arr[i] = item
    print(" ".join(map(str, arr)))

input()
arr = list(map(int, input().split()))
insert(arr)
