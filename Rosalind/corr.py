import sys

pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

def reverse(s):
    sc = ""
    for nt in reversed(s):
        sc += pairs[nt]
    return sc

def read_input():
    correct = set()
    incorrect = set()

    def add_entry(current_DNA):
        if current_DNA in incorrect or reverse(current_DNA) in incorrect:
            incorrect.discard(current_DNA)
            incorrect.discard(reverse(current_DNA))
            correct.add(current_DNA)
            correct.add(reverse(current_DNA))
        elif current_DNA not in correct:
            incorrect.add(current_DNA)
    
    input()
    current_DNA = ""
    for line in sys.stdin:
        if line[0] == ">":
            add_entry(current_DNA)
            current_DNA = ""
        else:
            current_DNA += line.strip()
    add_entry(current_DNA)
    return list(correct), list(incorrect)

def dist_hamming(A, B):
    ans = 0
    for a, b in zip(A, B):
        if a != b:
            ans += 1
    return ans

def dist_matrix(A, B, dist):
    return [[dist(a, b) for b in B] for a in A]

correct, incorrect = read_input()
D = dist_matrix(incorrect, correct, dist_hamming)

for i in range(len(incorrect)):
    for j in range(len(correct)):
        if D[i][j] == 1:
            print(f"{incorrect[i]}->{correct[j]}")
            break