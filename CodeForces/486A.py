N = int(input())
ans = (N+1)//2
if N%2 == 1:
    ans *= -1
print(ans)