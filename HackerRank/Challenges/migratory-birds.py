N = int(input())
S = list(map(int, input().split()))
S_dict = {}

for s in S:
    if s not in S_dict:
        S_dict[s] = 0
    S_dict[s] += 1

print(min(filter(lambda x: S_dict[x] == max(S_dict.values()), S_dict.keys())))

