memo = [0, 1]

N = int(input())
for n in range(2, N + 1):
    memo.append(memo[-1] + memo[-2])

print(memo[-1])