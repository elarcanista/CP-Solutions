def lisseq(lst, n, op):
    if memo[n] != 0:
        return memo[n]
    max_here = (1, [lst[n]])
    for i in range(n):
        prev = lisseq(lst, i, op)
        if op(lst[i], lst[n]) and prev[0] + 1 > max_here[0]:
            max_here = (prev[0] + 1, prev[1] + [lst[n]])
    
    global max_all
    if max_here[0] > max_all[0]:
        max_all = max_here
    memo[n] = max_here
    return max_here

n = int(input())
N = list(map(int, input().split()))
global max_all, memo
max_all = (1, [N[0]])
memo = [0] * (n+1)
memo[0] = (1, [N[0]])
lisseq(N, n-1, lambda x, y: x < y)
print(*max_all[1])
max_all = (1, [N[0]])
memo = [0] * (n+1)
memo[0] = (1, [N[0]])
lisseq(N, n-1, lambda x, y: x > y)
print(*max_all[1])
