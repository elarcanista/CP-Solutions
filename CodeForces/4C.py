names = {}

for _ in range(int(input())):
    name = input()
    if name not in names:
        names[name] = 0
        print("OK")
    else:
        names[name] += 1
        print(name, names[name], sep="")