for _ in range(int(input())):
    n, s, r = map(int, input().split())
    dice = [s - r]
    n -= 1
    while n > 0:
        dice.append(r//n)
        r -= dice[-1]
        n -= 1
    print(*dice)