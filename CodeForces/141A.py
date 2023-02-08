letter_count = {}
for s in input():
    if s not in letter_count:
        letter_count[s] = 0
    letter_count[s] += 1
for s in input():
    if s not in letter_count:
        letter_count[s] = 0
    letter_count[s] += 1
for s in input():
    if s not in letter_count:
        print("NO")
        break
    letter_count[s] -= 1
else:
    if sum(map(abs, letter_count.values())) == 0:
        print("YES")
    else:
        print("NO")