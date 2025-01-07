# https://www.hackerrank.com/challenges/ashton-and-string/

def counting_sort(arr, key, max_elem):
    count = [0 for _ in range(max_elem + 1)]
    ans = [0 for _ in range(len(arr))]
    for item in arr:
        count[key(item)] += 1
    for c in range(1, len(count)):
        count[c] += count[c - 1]
    for item in reversed(arr):
        count[key(item)] -= 1
        ans[count[key(item)]] = item
    return ans

def make_rank(suffix_arr, left_rank, right_rank):
    max_rank = 0
    rank = [0 for _ in range(len(suffix_arr))]
    for s in range(1, len(suffix_arr)):
        diff_left = left_rank(suffix_arr[s]) != left_rank(suffix_arr[s - 1])
        diff_right = right_rank(suffix_arr[s]) != right_rank(suffix_arr[s - 1])
        if diff_left or diff_right:
            max_rank += 1
        rank[suffix_arr[s]] = max_rank
    return rank, max_rank

def make_suffix_arr(text):
    suffix_arr = list(range(len(text)))
    min_elem = ord(min(text))
    rank = [ord(c) - min_elem for c in text]
    max_rank = max(rank)
    prefix = 1
    left_rank = lambda i: rank[i]
    right_rank = lambda i: rank[i + prefix] + 1 if i + prefix < len(rank) else 0
    while prefix < len(text):
        suffix_arr = counting_sort(suffix_arr, right_rank, max_rank + 1)
        suffix_arr = counting_sort(suffix_arr, left_rank, max_rank)
        rank, max_rank = make_rank(suffix_arr, left_rank, right_rank)
        if max_rank == len(rank) - 1:
            break
        prefix *= 2
    return suffix_arr, rank

def make_lcp_arr(text, suffix_arr, rank):
    lcp_arr = [0 for _ in range(len(suffix_arr))]
    common = 0
    for s in range(len(text)):
        if rank[s] == 0:
            continue
        t = suffix_arr[rank[s] - 1]
        m = max(s, t)
        while m + common < len(text) and text[s + common] == text[t + common]:
            common += 1
        lcp_arr[rank[s]] = common
        common -= common > 0
    return lcp_arr

def make_ans(text, suffix_arr, lcp_arr, k):
    acum = 0
    for i in range(len(suffix_arr)):
        s_length = len(text) - suffix_arr[i]
        segment_length = s_length * (s_length + 1) // 2
        common_length = lcp_arr[i] * (lcp_arr[i] + 1) // 2
        if k > acum + segment_length - common_length:
            acum += segment_length - common_length
            continue
        for j in range(lcp_arr[i] + 1, s_length + 1):
            if k > acum + j:
                acum += j
            else:
                return text[suffix_arr[i] + k - acum - 1]
    return -1

for _ in range(int(input())):
    text = input()
    k = int(input())
    suffix_arr, rank = make_suffix_arr(text)
    lcp_arr = make_lcp_arr(text, suffix_arr, rank)
    ans = make_ans(text, suffix_arr, lcp_arr, k)
    print(ans)
