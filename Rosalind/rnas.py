import sys

pairs = {"A": ["U"], "C": ["G"], "G": ["C", "U"], "U": ["A", "G"]}


def noncrossing(DNA):   
    if DNA in memo:
        return memo[DNA]
    if len(DNA) <= 4:
        return 1
    ans = noncrossing(DNA[1:])
    for i in range(4, len(DNA)):
        if DNA[i] in pairs[DNA[0]]:
            inside = noncrossing(DNA[1:i])
            outside = noncrossing(DNA[i+1:])
            ans += inside * outside
    memo[DNA] = ans
    return ans

memo = {"": 1}
DNA = input()
print(noncrossing(DNA))