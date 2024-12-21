# https://www.hackerrank.com/contests/projecteuler/challenges/euler063/
import math

N = int(input())

lower_bound = math.ceil((10 ** (N-1))**(1/N))
upper_bound = math.floor((10 ** N - 1)**(1/N))

for n in range(lower_bound, upper_bound+1):
    print(n**N)

