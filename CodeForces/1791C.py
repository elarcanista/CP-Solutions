for _ in range(int(input())):
    N = int(input())
    S = input()
    i = 0
    while i < len(S) // 2:
        if int(S[i]) + int(S[-i - 1]) != 1:
            break
        i += 1
    if i == 0:
        print(len(S))
    else:
        print(len(S[i: -i]))