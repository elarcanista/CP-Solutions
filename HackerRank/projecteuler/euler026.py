# https://www.hackerrank.com/contests/projecteuler/challenges/euler026/
max_N = 10**4

reps = [0] * (max_N + 1)

for n in range(1, len(reps)):
    rems = {}
    r = -1
    count = 0
    while r != 0 and r not in rems:
        rems[r] = count
        count += 1
        r = (10*r) % n
    if r != 0:
        reps[n] = count - rems[r]

def find(N):
    m = 0
    n = 0
    for i in range(N):
        if reps[i] > m:
            m = reps[i]
            n = i
    return n

for _ in range(int(input())):
    N = int(input())
    print(find(N))
