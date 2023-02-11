N, i = map(int, input().split())
S = list(map(int, input().split()))
p = int(input())
ans = p-(sum(S) - S[i])//2
if ans == 0:
    print("Bon Appetit")
else:
    print(ans)