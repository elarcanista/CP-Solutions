# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_diff = arr[-1] - arr[0]
for curr in range(1, len(arr)):
    new_diff = arr[curr] - arr[curr-1]
    if new_diff < min_diff:
        min_diff = new_diff
print(min_diff)
