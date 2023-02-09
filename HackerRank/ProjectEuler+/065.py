def convergent(N):
    num = 0
    den = 1

    for n in range(N, -1, -1):
        if n % 3 == 1:
            a = (n//3 + 1)*2
        else:
            a = 1
        num = a*(den) + num
        num, den = den, num
    return num + 2*den, den

N = int(input())

print(sum(map(int, list(str(convergent(N-2)[0])))))