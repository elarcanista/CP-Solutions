# https://www.hackerrank.com/challenges/string-similarity/

def counting_sort(arr, max_elem, key):
    ans = [0 for _ in range(len(arr))]
    count = [0 for _ in range(max_elem + 1)]
    for item in arr:
        count[key(item)] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for item in reversed(arr):
        count[key(item)] -= 1
        ans[count[key(item)]] = item
    return ans

def make_rank(suffix, left_rank, right_rank):
    max_rank = 0
    rank = [0 for _ in range(len(suffix))]
    for i in range(1, len(suffix)):
        diff_left = left_rank(suffix[i]) != left_rank(suffix[i - 1])
        diff_right = right_rank(suffix[i]) != right_rank(suffix[i - 1])
        if diff_left or diff_right:
            max_rank += 1
        rank[suffix[i]] = max_rank
    return rank, max_rank

def make_suffix(text):
    suffix = list(range(len(text)))
    min_elem = ord(min(text))
    rank = [ord(c) - min_elem for c in text]
    max_rank = max(rank)
    prefix = 1
    left_rank = lambda i: rank[i]
    right_rank = lambda i: rank[i + prefix] + 1 if i + prefix < len(rank) else 0
    while prefix < len(suffix):
        suffix = counting_sort(suffix, max_rank + 1, right_rank)
        suffix = counting_sort(suffix, max_rank, left_rank)
        rank, max_rank = make_rank(suffix, left_rank, right_rank)
        if max_rank == len(rank) - 1:
            break
        prefix *= 2
    return suffix, rank

def make_lcp(text, suffix, rank):
    common = 0
    lcp = [0 for _ in range(len(suffix))]
    for i in range(len(suffix)):
        if rank[i] == 0:
            continue
        j = suffix[rank[i] - 1]
        m = max(i, j)
        while m + common < len(text) and text[i + common] == text[j + common]:
            common += 1
        lcp[rank[i]] = common
        common -= common > 0
    return lcp

from math import inf

def similarity(rank, lcp):
    S = rank[0]
    acum = 0
    last = inf
    for i in reversed(range(S + 1)):
        last = min(last, lcp[i])
        acum += last
    last = inf
    for i in range(S + 1, len(lcp)):
        last = min(last, lcp[i])
        acum += last
    return acum + len(lcp)

for _ in range(int(input())):
    text = input()
    suffix, rank = make_suffix(text)
    lcp = make_lcp(text, suffix, rank)
    ans = similarity(rank, lcp)
    print(ans)
