N = int(input())

a = 0
b = 1    
for n in range(N+1):
    c = a + 2*b
    numerator = b+c
    denominator = c
    if len(str(numerator)) > len(str(denominator)):
        print(n + 1)
    a, b = b, c    