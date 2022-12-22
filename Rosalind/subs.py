DNA = input()
sub = input()
ans = []
for start in range(len(DNA) - len(sub) + 1):
    if sub == DNA[start:start + len(sub)]:
        ans.append(start + 1)

print(*ans)