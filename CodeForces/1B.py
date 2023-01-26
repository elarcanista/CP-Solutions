import re

def to_number(S):
    base = ord("Z") - ord("A") + 1
    pos_value = 1
    N = 0
    for c in S[::-1]:
        N += (ord(c) - ord("A") + 1) * pos_value
        pos_value *= base
    return N

def to_letter(N):
    base = ord("Z") - ord("A") + 1
    S = ""
    while N > 0:
        S += chr(ord("A") + (N - 1) % base)
        N = (N-1) // base
    return S[::-1]

for _ in range(int(input())):
    coords = input()
    match = re.fullmatch("R(\d+)C(\d+)", coords)
    if match is None:
        match = re.fullmatch("([A-Z]+)(\d+)", coords)
        r = match.group(2)
        c = to_number(match.group(1))
        print(f"R{r}C{c}")
    else:
        r = match.group(1)
        c = to_letter(int(match.group(2)))
        print(f"{c}{r}")
