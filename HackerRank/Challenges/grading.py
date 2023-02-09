def grade(N):
    if N < 38:
        return N
    if 5 - (N % 5) < 3:
        return N - (N % 5) + 5
    return N

for _ in range(int(input())):
    N = int(input())
    print(grade(N))