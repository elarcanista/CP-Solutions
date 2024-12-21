# https://www.hackerrank.com/challenges/manasa-and-stones/
for _ in range(int(input())):
    N = int(input())
    a = int(input())
    b = int(input())
    a, b = sorted([a, b])
    print(*list(set(i * b + (N - i - 1) * a for i in range(N))))
