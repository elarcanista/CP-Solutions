for _ in range(int(input())):
    x, y, z = map(int, input().split())
    dx = abs(x - z)
    dy = abs(y - z)
    if dx == dy:
        print("Mouse C")
    elif dx < dy:
        print("Cat A")
    else:
        print("Cat B")