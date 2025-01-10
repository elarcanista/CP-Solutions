# https://www.hackerrank.com/challenges/string-function-calculation/

def counting_sort(arr, max_elem, key):
    ans = [-1 for _ in arr]
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
    rank = [0 for _ in suffix]
    max_rank = 0
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
    right_rank = lambda i: rank[prefix + i] + 1 if prefix + i < len(rank) else 0
    while prefix < len(text):
        suffix = counting_sort(suffix, max_rank + 1, right_rank)
        suffix = counting_sort(suffix, max_rank, left_rank)
        rank, max_rank = make_rank(suffix, left_rank, right_rank)
        if max_rank == len(rank) - 1:
            break
        prefix *= 2
    return suffix, rank

def make_lcp(text, suffix, rank):
    lcp = [0 for _ in suffix]
    common = 0
    for i in range(len(text)):
        if rank[i] == 0:
            continue
        j = suffix[rank[i] - 1]
        m = max(i, j)
        while m + common < len(text) and text[i + common] == text[j + common]:
            common += 1
        lcp[rank[i]] = common
        common -= common > 0
    return lcp

def make_ans(lcp):
    stack = []
    ans = len(lcp)
    for i in range(1, len(lcp)):
        start = i
        while len(stack) > 0 and lcp[i] < stack[-1][1]:
            start, length = stack.pop()
            repeats = i - start + 1
            print(i, start, length, repeats, length * repeats)
            ans = max(ans, length * repeats)
        if len(stack) == 0 or lcp[i] > stack[-1][1]:
            stack.append((start, lcp[i]))
    while len(stack) > 0:
        start, length = stack.pop()
        repeats = len(lcp) - start + 1
        print(i, start, length, repeats, length * repeats)
        ans = max(ans, length * repeats)
    return ans

text = input()
suffix, rank = make_suffix(text)
print([text[i:] for i in suffix])
lcp = make_lcp(text, suffix, rank)
print(lcp)
ans = make_ans(lcp)
print(ans)
