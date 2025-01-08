# https://www.hackerrank.com/challenges/find-strings/

def counting_sort(arr, max_elem, key):
    ans = [0 for _ in arr]
    count = [0 for _ in range(max_elem + 1)]
    for item in arr:
        count[key(item)] += 1
    for c in range(1, len(count)):
        count[c] += count[c - 1]
    for item in reversed(arr):
        count[key(item)] -= 1
        ans[count[key(item)]] = item
    return ans

def make_rank(suffix, left_rank, right_rank):
    max_rank = 0
    rank = [max_rank for _ in suffix]
    for s in range(1, len(suffix)):
        diff_left = left_rank(suffix[s]) != left_rank(suffix[s - 1])
        diff_right = right_rank(suffix[s]) != right_rank(suffix[s - 1])
        if diff_left or diff_right:
            max_rank += 1
        rank[suffix[s]] = max_rank
    return rank, max_rank

def make_suffix_arr(text):
    suffix = list(range(len(text)))
    min_elem = ord(min(text))
    rank = [ord(c) - min_elem for c in text]
    max_rank = max(rank)
    prefix = 1
    left_rank = lambda i: rank[i]
    right_rank = lambda i: rank[i + prefix] + 1 if i + prefix < len(rank) else 0
    while prefix < len(rank):
        suffix = counting_sort(suffix, max_rank + 1, right_rank)
        suffix = counting_sort(suffix, max_rank, left_rank)
        rank, max_rank = make_rank(suffix, left_rank, right_rank)
        if max_rank == len(rank) - 1:
            break
        prefix *= 2
    return suffix, rank

def make_lcp_arr(text, suffix, rank, sep):
    lcp_arr = [0 for _ in suffix]
    common = 0
    for i in range(len(text)):
        if rank[i] == 0:
            continue
        j = suffix[rank[i] - 1]
        m = max(i, j)
        while m + common < len(text) and text[i + common] == text[j + common] and text[i + common] != sep:
            common += 1
        lcp_arr[rank[i]] = common
        common -= common > 0
    return lcp_arr

def binary_search(arr, target):
    left, right = 0, len(arr)
    while left != right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def make_ans(text, separators, suffix, lcp, k):
    acum = 0
    for s in range(len(suffix)):
        ending = separators[binary_search(separators, suffix[s])]
        subs_size = ending - suffix[s]
        if subs_size == 0:
            continue
        total_size = subs_size - lcp[s]
        if k > acum + total_size:
            acum += total_size
            continue
        return text[suffix[s]: suffix[s] + lcp[s] + k - acum]
    return "INVALID"

arr = []
for _ in range(int(input())):
    arr.append(input())
# Combine strings
sep = min([min(s) for s in arr])
sep = chr(ord(sep) - 1)
separators = [-1]
text = ""
for item in arr:
    text += item + sep
    separators.append(len(text) - 1)
# Calculate suffix and LCP arrays
suffix, rank = make_suffix_arr(text)
lcp = make_lcp_arr(text, suffix, rank, sep)
# Calculate k-th lexicographical substring
for _ in range(int(input())):
    k = int(input())
    ans = make_ans(text, separators, suffix, lcp, k)
    print(ans)
