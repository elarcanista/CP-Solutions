# https://www.hackerrank.com/challenges/save-the-prisoner/
for _ in range(int(input())):
    n, m, s = map(int, input().split())
    ans = (s - 1 + m) % n
    print(ans if ans != 0 else n)
