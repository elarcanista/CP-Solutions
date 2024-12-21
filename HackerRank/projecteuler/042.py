# https://www.hackerrank.com/contests/projecteuler/challenges/euler042/
def triang_inverse(t):
    N = (-1 + (1+8*t)**(1/2))/2
    if int(N) == N:
        return int(N)
    else:
        return -1

for _ in range(int(input())):
    N = int(input())
    print(triang_inverse(N))
