N = int(input())
p = int(input())

front = p//2

back = (N - p // 2 * 2) // 2

print(min(front, back))