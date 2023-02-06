N = int(input())
S = map(int, input().split())
for s in S:
    if s == 1:
        print("HARD")
        break
else:
    print("EASY")