X = [0, 0, 0]
for _ in range(int(input())):
    for i, y in enumerate(map(int, input().split())):
        X[i] += y
if X == [0, 0, 0]:
    print("YES")
else:
    print("NO")