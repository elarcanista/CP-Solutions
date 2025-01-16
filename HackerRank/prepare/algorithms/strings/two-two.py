# https://www.hackerrank.com/challenges/two-two/
from collections import deque

def make_powers(base, exponent):
    ans = [1]
    for i in range(1, exponent + 1):
        ans.append(ans[-1] * base)
    return ans

def make_key_tree(keys):
    tree = [{}]
    matches = {}
    depth = [0]
    for i, k in enumerate(keys):
        curr_node = c = 0
        while c < len(k) and k[c] in tree[curr_node]:
            curr_node = tree[curr_node][k[c]]
            c += 1
        while c < len(k):
            tree[curr_node][k[c]] = len(tree)
            depth.append(depth[curr_node] + 1)
            curr_node = len(tree)
            tree.append({})
            c += 1
        matches[curr_node] = i
    return tree, matches, depth

def bfs(tree, f):
    ans = [0 for _ in tree]
    q = deque()
    q.append((0, "", 0))
    while len(q) > 0:
        par_node, par_char, curr_node = q.popleft()
        for next_char, next_node in tree[curr_node].items():
            q.append((curr_node, next_char, next_node))
        ans[curr_node] = f(ans, par_node, par_char, curr_node)
    return ans

def failure_induction(tree, failure, par_node, par_char, curr_node):
    if par_node == 0:
        return 0
    par_failure = failure[par_node]
    while par_failure != 0 and par_char not in tree[par_failure]:
        par_failure = failure[par_failure]
    if par_char in tree[par_failure]:
        return tree[par_failure][par_char]
    else:
        return 0

def subkey_induction(failure, matches, subkey, curr_node):
    if failure[curr_node] in matches:
        return failure[curr_node]
    return subkey[failure[curr_node]]

def aho_corasick(tree, failure, subkey, matches, text):
    ans = []
    curr_node = c = 0
    while c < len(text):
        while c < len(text) and text[c] in tree[curr_node]:
            curr_node = tree[curr_node][text[c]]
            if curr_node in matches:
                ans.append((c, matches[curr_node]))
            subkey_node = subkey[curr_node]
            while subkey_node != 0:
                ans.append((c, matches[subkey_node]))
                subkey_node = subkey[subkey_node]
            c += 1
        if curr_node == 0:
            c += 1
        else:
            curr_node = failure[curr_node]
    return ans

powers = list(map(str, make_powers(2, 800)))
# print(powers)
tree, matches, depth = make_key_tree(powers)
# print(matches)
# for i, k in enumerate(tree):
#     print(i, depth[i], k)
failure = bfs(tree,
              lambda a, u, c, v: failure_induction(tree, a, u, c, v))
# for i, k in enumerate(failure):
#     print(i, k)
subkey = bfs(tree,
             lambda a, u, c, v: subkey_induction(failure, matches, a, v))
# for i, k in enumerate(subkey):
#     print(i, k)
for _ in range(int(input())):
    text = input()
    ans = aho_corasick(tree, failure, subkey, matches, text)
    print(len(ans))
