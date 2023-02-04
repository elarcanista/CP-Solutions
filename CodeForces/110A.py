def lucky(N):
    for c in str(N):
        if c not in ["4", "7"]:
            return False
    return True

def nearly(N):
    ans = 0
    for c in str(N):
        if c in ["4", "7"]:
            ans += 1
    return lucky(ans)

N = int(input())
if nearly(N):
    print("YES")
else: 
    print("NO")