max_N = 28123

S = [False] * (max_N + 1)
div_sum = [1] * (max_N + 1)
div_sum[0] = 0
abundant = set()

p = 2
while p <= max_N:
    for kp in range(2*p, max_N, p):
        div_sum[kp] += p
        if div_sum[kp] > kp:
            abundant.add(kp)
    p += 1

abundant = sorted(list(abundant))
for p in abundant:
    for q in abundant:
        if p + q < len(S):
            S[p + q] = True
        else:
            break

#print(abundant)
for _ in range(int(input())):
    N = int(input())
    if N > max_N or S[N]:
        print("YES")
    else:
        print("NO")