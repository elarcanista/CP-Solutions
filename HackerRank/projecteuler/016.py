# https://www.hackerrank.com/contests/projecteuler/challenges/euler016/
for _ in range(int(input())):
    N = int(input())
    print(sum(map(int, list(str(2**N)))))
