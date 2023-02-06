hello = "hello"
i = 0
for c in input():
    if c == hello[i]:
        i += 1
    if i >= len(hello):
        print("YES")
        break
else:
    print("NO")