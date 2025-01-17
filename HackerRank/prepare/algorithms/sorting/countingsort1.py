input()
arr = map(int, input().split())
count = [0 for _ in range(100)]
for item in arr:
    count[item] += 1
print(" ".join(map(str, count)))
