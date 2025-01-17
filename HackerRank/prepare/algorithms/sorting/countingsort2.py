# https://www.hackerrank.com/challenges/countingsort2/
def counting_sort(arr, max_elem):
    ans = list(range(len(arr)))
    count = [0 for _ in range(max_elem)]
    for item in arr:
        count[item] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for item in reversed(arr):
        count[item] -= 1
        ans[count[item]] = item
    return ans

input()
arr = list(map(int, input().split()))
arr = counting_sort(arr, 100)
print(" ".join(map(str, arr)))
