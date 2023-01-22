import sys

def read_input():
    A = ""
    input()
    curr = ""
    for line in sys.stdin:
        if line[0] == ">":
            A = curr
            curr = ""
        else:
            curr += line.strip()
    return A, curr

def dist(A, B):
    if (A, B) in memo:
        return memo[(A, B)]
    if len(A) == 0:
        return len(B)
    if len(B) == 0:
        return len(A)
    if A[0] == B[0]:
        return dist(A[1:], B[1:])
    d = 1 + min(dist(A[1:], B), dist(A, B[1:]), dist(A[1:], B[1:]))
    memo[(A, B)] = d
    return d

memo = {}
A, B = read_input()
for i in reversed(range(min(len(A), len(B)))):
    dist(A[i:], B[i:])
print(dist(A, B))