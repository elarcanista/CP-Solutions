DNA = (list(input()), list(input()))

distance = 0
for a, b in zip(*DNA):
    if a != b:
        distance += 1
print(distance)