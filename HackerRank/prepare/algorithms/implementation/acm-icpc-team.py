# https://www.hackerrank.com/challenges/acm-icpc-team/
N, _ = map(int, input().split())
members = []
for _ in range(N):
    members.append(int(input(), 2))
max_or = 0
num_max = 0
for i in range(len(members)):
    for j in range(i+1, len(members)):
        if bin(members[i] | members[j]).count("1") > max_or:
            max_or = bin(members[i] | members[j]).count("1")
            num_max = 1
        elif bin(members[i] | members[j]).count("1") == max_or:
            num_max += 1
print(max_or, num_max, sep="\n")
