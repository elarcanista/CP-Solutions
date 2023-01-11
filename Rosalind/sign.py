import itertools as iter

def factorial(N):
    ans = 1
    for n in range(1, N+1):
        ans *= n
    return ans

N = int(input())
print(factorial(N) * (2**N))
for perm in iter.permutations(range(1,N+1)):
    for sign in iter.product([-1,1], repeat=N):
        print(*map(lambda x: x[0]*x[1], zip(perm, sign)))