# https://www.hackerrank.com/contests/projecteuler/challenges/euler074/
def factorial(n):
    count = 1
    for i in range(2, n+1):
        count *= i
    return count

def next_i(n, fact):
    acum = 0
    while n != 0:
        acum += fact[n % 10]
        n //= 10
    return acum

def graph_fill(curr, graph, rank, inv_rank, fact):
    stack = []
    while curr not in graph:
        stack.append(curr)
        graph[curr] = next_i(curr, fact)
        curr = graph[curr]
    while len(stack) > 0:
        prev = stack.pop()
        if prev == curr:
            rank[prev] = 1
        else:
            rank[prev] = rank[curr] + 1
        if rank[prev] not in inv_rank:
            inv_rank[rank[prev]] = []
        inv_rank[rank[prev]].append(prev)
        curr = prev

def pretty_print(n, graph, rank):
    hist = []
    while n not in hist:
        hist.append(n)
        n = graph[n]
    for i in range(len(hist)):
        hist[i] = f"({hist[i]}: {rank[hist[i]]})"
    return ", ".join(hist)

def bin_search(arr, n):
    left, right = -1, len(arr) - 1
    mid = (left + right + 1)//2
    while left != right and mid != 0:
        if arr[mid] > n:
            right = mid - 1
        elif arr[mid] <= n:
            left = mid
        mid = (left + right + 1)//2
    if mid == 0 and arr[mid] == n:
        return mid
    return left 

graph = {
    169: 363601, 363601: 1454, 1454: 169,
    871: 45361, 45361: 871,
    872: 45362, 45362: 872,
    0: 1, 1: 1, 2: 2
}
rank = {
    169: 3, 363601: 3, 1454: 3,
    871: 2, 45361: 2,
    872: 2, 45362: 2,
    0: 2, 1: 1, 2: 1
}
inv_rank = {
    1: [1, 2],
    2: [871, 45361, 872, 45362, 0],
    3: [169, 363601, 1454]
}

fact = [factorial(i) for i in range(10)]
next_fill = 3
T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    for i in range(next_fill, N+1):
        graph_fill(i, graph, rank, inv_rank, fact)
    next_fill = max(next_fill, N+1)
    if L not in inv_rank:
        print(-1)
        continue
    inv_rank[L].sort()
    index = bin_search(inv_rank[L], N)
    if index == -1:
        print(-1)
        continue
    print(" ".join(map(str, inv_rank[L][:index + 1])))
