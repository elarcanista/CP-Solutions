R, C = map(int, input().split())

for r in range(R):
    if r % 2 == 0:
        print("#"*C)
    elif r % 4 == 1:
        print("." * (C-1) + "#")
    else:
        print("#" + "." * (C-1))