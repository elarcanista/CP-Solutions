N, K = map(int, input().split())
if K > (N+1)//2:
    K -= (N+1)//2
    print(2*K)
else:
    print(K*2 - 1)