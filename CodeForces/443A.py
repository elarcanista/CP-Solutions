S = input()[1:-1]

if len(S) == 0:
    print(0)
else:
    print(len(set(S.split(", "))))