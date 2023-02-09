max_N = 10**6
max_K = 9999

mem = [1] * (max_N + max_K + 1)

for n in range(1, len(mem)):
    mem[n] = mem[n-1] + 3*n + 1

N, K = map(int, input().split())

for n in range(N):    
    Pn1 = mem[n] - mem[n-K]
    Pn1 = 0 if Pn1 < 0 else Pn1
    Pn2 = mem[n] + mem[n-K]
    n1 = (1 + (1 + 24*Pn1)**(1/2))/6
    n2 = (1 + (1 + 24*Pn2)**(1/2))/6
    if n1 == int(n1) or n2 == int(n2):
        print(mem[n])