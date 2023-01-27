pi = "314159265358979323846264338327"
for _ in range(int(input())):
    approx = input()
    i = 0
    while i < len(approx):
        if pi[i] != approx[i]:
            break
        i += 1
    print(i)