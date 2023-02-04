for _ in range(int(input())):
    N = int(input())
    S = input()
    coords = 0
    moves = {"U": 1j, "D": -1j, "L": -1, "R": 1}
    chocolate = 1 + 1j
    for c in S:
        coords += moves[c]
        if coords == chocolate:
            print("YES")
            break
    else:
        print("NO")