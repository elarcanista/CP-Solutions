S = input()
last = ""
ans = 1
for s in S:
    if s == last:
        ans += 1
    else:
        ans = 1
    if ans >= 7:
        print("YES")
        break
    last = s
else:
    print("NO")