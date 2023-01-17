import sys
import itertools as iter

def read_input():
    input()
    current_DNA = ""
    for line in sys.stdin:
        current_DNA += line.strip()
    return current_DNA

def get_index(kmer):
    value = {"A": 1, "C": 2, "G": 3, "T": 4}
    ans = 0
    base = 1
    for c in reversed(kmer):
        ans += value[c] * base
        base *= 4
    return ans - 85

DNA = read_input()
composition = [0] * (4**4)
curr = DNA[:4]
composition[get_index(curr)] += 1
for c in DNA[4:]:
    curr = curr[1:] + c
    composition[get_index(curr)] += 1

print(*composition)

