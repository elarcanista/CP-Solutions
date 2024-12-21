# https://www.hackerrank.com/contests/projecteuler/challenges/euler022/
name = []
score = {}
for T in range(int(input())):
    name.append(input().lower())
name = sorted(name)

for T in range(len(name)):
    score[name[T]] = sum(map(lambda c: 
        ord(c.lower()) - ord('a') + 1, name[T])) * (T+1)

for _ in range(int(input())):
    print(score[input().lower()])
