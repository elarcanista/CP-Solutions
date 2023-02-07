last = ""
ans = 0
for _ in range(int(input())):
    magnet = input()
    if last != magnet:
        ans += 1
        last = magnet
print(ans)