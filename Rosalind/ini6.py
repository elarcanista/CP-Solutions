line = input().split()

count = {}

for word in line:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, c in count.items():
    print(word, c)