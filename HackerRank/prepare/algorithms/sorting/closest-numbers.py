# https://www.hackerrank.com/challenges/closest-numbers/
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_diff = arr[-1] - arr[0]
min_arr = []
for curr in range(1, len(arr)):
    new_diff = arr[curr] - arr[curr-1]
    if new_diff == min_diff:
        min_arr.append((arr[curr-1], arr[curr]))
    if new_diff < min_diff:
        min_arr = [(arr[curr-1], arr[curr])]
        min_diff = new_diff
min_arr = map(lambda x: f"{x[0]} {x[1]}", min_arr)
print(" ".join(min_arr))
