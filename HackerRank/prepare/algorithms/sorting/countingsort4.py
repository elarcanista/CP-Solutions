# https://www.hackerrank.com/challenges/countingsort4/
def counting_sort(arr, max_elem, key):
    ans = list(range(len(arr)))
    count = [0 for _ in range(max_elem)]
    for item in arr:
        count[key(item)] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for item in reversed(arr):
        count[key(item)] -= 1
        ans[count[key(item)]] = item
    return ans

arr = []
size = int(input())
for i in range(size):
    index, text = input().split()
    if i < size // 2:
        text = "-"
    arr.append((int(index), text))
arr = counting_sort(arr, 100, lambda t: t[0])
print(" ".join(map(lambda t: t[1], arr)))
