def lucky(N):
    for c in str(N):
        if c not in ["4", "7"]:
            return False
    return True

N = int(input())
for i in range(4, N+1):
    if N % i == 0 and lucky(i):
        print("YES")
        break
else:
    print("NO")