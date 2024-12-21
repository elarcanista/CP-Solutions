# https://www.hackerrank.com/challenges/append-and-delete/
def common(A, B):
    ans = ""
    for a, b in zip(A, B):
        if a != b:
            break
        ans += a
    return ans

def check(A, B, N):
    if N >= len(A) + len(B):
        return True

    C = common(A, B)
    moves = len(A) + len(B) - 2*len(C)
    if moves <= N and (N - moves) % 2 == 0:
        return True
    
    return False

A = input()
B = input()
N = int(input())
if check(A, B, N):
    print("Yes")
else:
    print("No")
