N, K = map(int, input().split())
for n in range(2, N):
    i = 1
    pan = str(n)
    while len(pan) == len(set(pan)):
        if set(pan) == {str(k) for k in range(1, K+1)}:
            print(n)
            break
        i += 1
        pan += str(n*i)
        