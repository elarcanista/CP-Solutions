N = int(input()) + 1
while len(str(N)) != len(set(str(N))):
    N += 1
print(N)