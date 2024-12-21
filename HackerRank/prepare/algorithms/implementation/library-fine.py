# https://www.hackerrank.com/challenges/library-fine/
def fine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    return 0
        
d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
print(fine(d1, m1, y1, d2, m2, y2))
