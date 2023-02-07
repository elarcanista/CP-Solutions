S = input()
ans = ""
i = 0
while i < len(S):
    try:
        j = S.index("WUB", i)
    except:
        ans += S[i:]
        break
    if i != j:
        ans += S[i: j] + " "
    i = j + 3
print(ans.strip())