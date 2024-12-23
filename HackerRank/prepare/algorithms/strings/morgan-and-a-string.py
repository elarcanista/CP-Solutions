# https://www.hackerrank.com/challenges/morgan-and-a-string/
def get(A, B, i, j, memo):
    ans = ""
    while i < len(A) or j < len(B):
        if (i, j) not in memo:
            i, j = j, i
        if memo[(i, j)]:
            ans += A[i]
            i += 1
        else:
            ans += B[j]
            j += 1
    return ans

def lex_min(A, B, memo):
    def symmetry(i, j):
        return (j, i) in memo and A[i::] == B[i::] and A[j::] == B[j::]
    stack = [(0, 0, False)]
    while len(stack) > 0:
        i, j, resume = stack.pop()
        if (i, j) in memo or symmetry(i, j):
            continue
        if not resume:
            stack.append((i, j, True))
            if A[i] <= B[j]:
                stack.append((i + 1, j, False))
            if B[j] <= A[i]:
                stack.append((i, j + 1, False))
        else:
            if A[i] < B[j]:
                memo[(i, j)] = True
            elif B[j] < A[i]:
                memo[(i, j)] = False
            else:
                pathA = get(A, B, i + 1, j, memo)
                pathB = get(A, B, i, j + 1, memo)
                if pathA <= pathB:
                    memo[(i, j)] = True
                else:
                    memo[(i, j)] = False 
    return get(A, B, 0, 0, memo)

# def lex_min(A, B, i, j, memo):
#     if (i, j) in memo:
#         return memo[(i, j)]
#     if (j, i) in memo and A[i::] == B[i::] and A[j::] == B[j::]:
#         return memo[(j, i)]
#     if i == len(A):
#         ans = B[j::]
#     elif j == len(B):
#         ans = A[i::]
#     elif A[i] < B[j]:
#         ans = A[i] + lex_min(A, B, i + 1, j, memo)
#     elif B[j] < A[i]:
#         ans = B[j] + lex_min(A, B, i, j + 1, memo)
#     else:
#         pathA = lex_min(A, B, i + 1, j, memo)
#         pathB = lex_min(A, B, i, j + 1, memo)
#         if pathA <= pathB:
#             ans = A[i] + pathA
#         else:
#             ans = B[j] + pathB
#     memo[(i, j)] = ans
#     return ans

for _ in range(int(input())):
    A = input()
    B = input()
    memo = {}
    for i in range(len(A) + 1):
        memo[(i, len(B))] = True
    for j in range(len(B) + 1):
        memo[(len(A), j)] = False
    print(lex_min(A, B, memo))
