x = 0
for _ in range(int(input())):
    line = input()
    if "++" in line:
        x += 1
    else:
        x -= 1
print(x)