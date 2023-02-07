N = int(input())
S = set(list(map(int, input().split()))[1:])
S = S.union(set(list(map(int, input().split()))[1:]))
if len(S) == N:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")