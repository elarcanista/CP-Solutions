import sys

def fact(N):
    ans = 1
    for n in range(2, N+1):
        ans *= n
    return ans

DNA = ""

input()
for line in sys.stdin:
    DNA += line.strip()

print(fact(DNA.count("A")) * fact(DNA.count("C")))