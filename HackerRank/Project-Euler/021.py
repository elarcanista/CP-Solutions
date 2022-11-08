def div_sum(N):
    ans = [1]*(N+1)
    ans[:3] = [0, 1, 1]
    p = 2
    while p < N/2:
        for kp in range(2*p, N, p):
            ans[kp] += p
        p += 1
    return ans

def cum_sum(S):
    acum = 0
    ans = [1] * len(S)
    for i in range(len(S)):
        ans[i] = acum
        if S[i] != i:
            if S[i] < len(S) and S[S[i]] == i:
                acum += i
    return ans
        
S = div_sum(10**5+1)
S2 = cum_sum(S)

for _ in range(int(input())):
    N = int(input())
    print(S2[N])