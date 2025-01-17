# https://www.hackerrank.com/challenges/countingsort3/
def counting_sort(arr, max_elem, key):
    ans = list(range(len(arr)))
    count = [0 for _ in range(max_elem)]
    for item in arr:
        count[key(item)] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    return count

arr = []
for _ in range(int(input())):
    index, text = input().split()
    arr.append((int(index), text))
count = counting_sort(arr, 100, lambda t: t[0])
print(" ".join(map(str, count)))
