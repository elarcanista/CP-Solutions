A = input()
B = input()
C = ""
for a, b in zip(A, B):
    C += str(int(a) ^ int(b))
print(C)