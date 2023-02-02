N, K = input().split()
K = int(K)

k = 0
while k < K:
    for i in range(len(N) - 1):
        if N[i] < N[i+1]:
            N = N[:i] + N[i+1:]
            k += 1
            break
    else:
        break

print(N[:len(N)-(K-k)])