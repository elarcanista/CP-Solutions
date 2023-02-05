for _ in range(int(input())):
    N = int(input())
    N -= 1
    A = 1
    B = 0
    curr = 2 
    while N >= curr:
        if curr % 4 > 1:
            B += curr
        else:
            A += curr
        N -= curr
        curr += 1
    if curr % 4 > 1:
        B += N
    else:
        A += N
    print(A, B)