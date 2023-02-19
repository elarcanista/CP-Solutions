def kaprekar(N):
    N2 = str(N**2)
    d = len(str(N))
    if len(N2[-d]) != len(str(int(N2[-d]))):
        return False
    i = len(N2)-d
    l = int(N2[:i]) if len(N2[:i]) > 0 else 0
    r = int(N2[-d:])
    if l + r == N:
        return True
    return False

p = int(input())
q = int(input())
ans = []
for N in range(p, q+1):
    if kaprekar(N):
        ans.append(N)
if len(ans) == 0:
    print("INVALID RANGE") 
else:
    print(*ans)