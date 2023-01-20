import sys

pairs = {"A": "U", "C": "G", "G": "C", "U": "A"}

def read_input():
    input()
    current_DNA = ""
    for line in sys.stdin:
        current_DNA += line.strip()
    return current_DNA

def noncrossing(DNA):
    if DNA in memo:
        return memo[DNA]
    ans = noncrossing(DNA[1:])
    for i in range(1, len(DNA)):
        if pairs[DNA[0]] == DNA[i]:
            inside = noncrossing(DNA[1:i])
            outside = noncrossing(DNA[i+1:])
            ans += inside * outside
    memo[DNA] = ans
    return ans

memo = {"": 1}
DNA = read_input()
print(noncrossing(DNA) % 1000000)