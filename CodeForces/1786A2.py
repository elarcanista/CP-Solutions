for _ in range(int(input())):
    N = int(input())
    N -= 1
    A = 1
    B = 0
    curr = 2 
    A2 = 1
    B2 = 0
    while N >= curr:
        if curr % 4 > 1:
            B += curr
            B2 += curr // 2
        else:
            A += curr
            A2 += (curr + 1) // 2
        N -= curr
        curr += 1
    if curr % 4 > 1:
        B += N
        B2 += N // 2
    else:
        A += N
        A2 += (N + 1) // 2
    print(A2, A - A2, B2, B - B2)