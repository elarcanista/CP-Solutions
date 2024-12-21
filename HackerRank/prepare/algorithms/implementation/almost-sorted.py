# https://www.hackerrank.com/challenges/almost-sorted/
N = int(input())
L = list(map(int, input().split()))
sL = sorted(L)
indices = []
for i, (l, sl) in enumerate(zip(L, sL)):
    if l != sl:
        indices.append(i)
if len(indices) == 0:
    print("yes")
elif len(indices) == 2:
    print("yes")
    print("swap", indices[0] + 1, indices[1] + 1)
elif len(indices) > 2 and all([L[i] < L[i+1] for i in indices[:-1]]):
    print("yes")
    print("reverse", indices[0] + 1, indices[-1] + 1)
else:
    print("no")
