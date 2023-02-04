for _ in range(int(input())):
    N = int(input())
    S = input()
    A, B = {S[0]}, {}
    for c in S[1:]:
        if c not in B:
            B[c] = 0
        B[c] += 1
    max_s = len(A) + len(B)
    curr = max_s
    for c in S[1:-1]:
        if c not in A:
            curr += 1
            A.add(c)
        B[c] -= 1
        if B[c] == 0:
            curr -= 1
        max_s = max(curr, max_s)
    print(max_s)