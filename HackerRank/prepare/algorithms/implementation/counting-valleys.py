# https://www.hackerrank.com/challenges/counting-valleys/
N = int(input())
S = input()
height = 0
ans = 0
for s in S:
    if s == "U":
        height += 1
        if height == 0:
            ans += 1
    else:
        height -= 1
print(ans)
