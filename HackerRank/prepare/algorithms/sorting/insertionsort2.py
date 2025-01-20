# https://www.hackerrank.com/challenges/insertionsort1/
def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i
        while j > 0 and arr[j - 1] >= item:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item
        print(" ".join(map(str, arr)))

input()
arr = list(map(int, input().split()))
insertion_sort(arr)
