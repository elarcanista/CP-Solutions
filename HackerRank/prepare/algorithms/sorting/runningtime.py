# https://www.hackerrank.com/challenges/runningtime/
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr, count

input()
arr = list(map(int, input().split()))
print(insertion_sort(arr)[1])
