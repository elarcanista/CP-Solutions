# https://www.hackerrank.com/challenges/repeated-string/
S = input()
N = int(input())
ans = (N // len(S)) * S.count("a")
ans += S[:N%len(S)].count("a")
print(ans)
