alphabet = input().split()
N = int(input())

ans = []

def all_iters(prev):
    if len(prev) >= N:
        return
    for c in alphabet:
        print(prev + c)
        all_iters(prev + c)

all_iters("")