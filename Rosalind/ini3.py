line = input()

a, b, c, d = map(int, input().split())
print(line[a:b+1], line[c:d+1])