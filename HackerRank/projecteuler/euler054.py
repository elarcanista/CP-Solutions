# https://www.hackerrank.com/contests/projecteuler/challenges/euler054/
value_map = dict(zip(["T", "J", "Q", "K", "A"], range(10, 15)))
suit_map = dict(zip(["H", "C", "S", "D"], range(4)))

def parse(tokens):
    value_fst = [0] * 15
    suit_fst = [0] * 4
        
    for t in tokens:
        v = value_map[t[0]] if t[0] in value_map else int(t[0])
        s = suit_map[t[1]]

        value_fst[v] |= 1 << s
        suit_fst[s] |= 1 << v
    return value_fst, suit_fst

def repeat(vf, sf):
    count = [0,0,0]
    max_card = [0,0,0]
    for i, v in enumerate(vf):
        if bin(v).count("1") == 2:
            count[0] += 1
            max_card[0] = i
        if bin(v).count("1") == 3:
            count[1] += 1
            max_card[1] = i
        if bin(v).count("1") == 4:
            count[2] += 1
            max_card[2] = i
    return count, max_card

def straight(vf, sf):
    v = sf[0] | sf[1] | sf[2] | sf[3]
    if v & (1 << 14) != 0:
        v |= 1 << 1
    mask = (1 << 5) - 1
    mask <<= 10
    while bin(mask).count("1") == 5:
        if v & mask == mask:
            return mask.bit_length()
        mask >>= 1
    return 0

def flush(vf, sf):
    for s in sf:
        if bin(s).count("1") == 5:
            return s.bit_length()
    return 0

def play(hands):
    r, s, f = [], [], []
    for h in hands:
        r.append(repeat(*h))
        s.append(straight(*h))
        f.append(flush(*h))

    rule = lambda i: s[i] == 14 and f[i] # Royal flush
    if rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: s[i] and f[i] # Straight Flush
    if rule(0) and rule(1):
        if s[0] != s[1]:
            return s[0] < s[1]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: r[i][0][2] # Four of a Kind
    if rule(0) and rule(1):
        if r[0][1][2] != r[1][1][2]:
            return r[0][1][2] < r[1][1][2]
    elif rule(0):
        return 0
    elif rule(1):
        return 1
    
    rule = lambda i: r[i][0][0] and r[i][0][1] # Full House
    if rule(0) and rule(1):
        if r[0][1][1] != r[1][1][1]:
            return r[0][1][1] < r[1][1][1]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: f[i] # Flush
    if rule(0) and rule(1):
        if f[0] != f[1]:
            return f[0] < f[1]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: s[i] # Straight
    if rule(0) and rule(1):
        if s[0] != s[1]:
            return s[0] < s[1]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: r[i][0][1] # Three of a Kind
    if rule(0) and rule(1):
        if r[0][1][1] != r[1][1][1]:
            return r[0][1][1] < r[1][1][1]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: r[i][0][0] == 2 # Two Pairs
    if rule(0) and rule(1):
        if r[0][1][0] != r[1][1][0]:
            return r[0][1][0] < r[1][1][0]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    rule = lambda i: r[i][0][0] == 1 # One Pair
    if rule(0) and rule(1):
        if r[0][1][0] != r[1][1][0]:
            return r[0][1][0] < r[1][1][0]
    elif rule(0):
        return 0
    elif rule(1):
        return 1

    v0 = hands[0][1][0] | hands[0][1][1] | hands[0][1][2] | hands[0][1][3]
    v1 = hands[1][1][0] | hands[1][1][1] | hands[1][1][2] | hands[1][1][3]
    while v0.bit_length() == v1.bit_length():
        v0 &= ~(1 << v0.bit_length() -1)
        v1 &= ~(1 << v1.bit_length() -1)
    return v0.bit_length() < v1.bit_length()

for _ in range(int(input())):
    line = input().split()
    hand1 = parse(line[:5])
    hand2 = parse(line[5:])
    p = play([hand1, hand2])
    if p == 0:
        print("Player 1")
    else:
        print("Player 2")
