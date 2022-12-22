fib = [1, 1]
N, K = map(int, input().split())
for n in range(2, N):
    fib.append(K*fib[-2] + fib[-1])
print(fib[-1])