def rank(p, q, n):
    T = [(i * p) // q for i in range(n+1)]
    for i in range(2, len(T)):
        k = 2
        while i * k < len(T):
            T[i * k] -= T[i]
            k += 1
    return sum(T)

A, D = map(int, input().split())
print(rank(1, A, D) - rank(1, A+1, D) - 1)
