# https://www.hackerrank.com/challenges/taum-and-bday/
for _ in range(int(input())):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    wc = min(wc, bc+z)
    bc = min(bc, wc+z)
    print(b*bc + w*wc)
