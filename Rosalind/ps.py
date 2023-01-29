N = int(input())
H = sorted(list(map(int, input().split())))
K = int(input())

print(*H[:K])