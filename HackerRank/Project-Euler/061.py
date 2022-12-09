import math

def search_cycle(P, lst):
    ans = []
    if len(P) == 0 and lst[-1] % 100 == lst[0] // 100:
        return [lst]
    for p in P:
        link = lst[-1] % 100
        lower_n = math.ceil(inverse(p, link*100))
        upper_n = math.floor(inverse(p, link*100 + 99))
        for n in range(lower_n, upper_n+1):
            N = pgon(p, n)
            if N % 100 < 10 or N < 1000:
                continue    
            P2 = P.copy()
            P2.remove(p)
            ans.extend(search_cycle(P2, [*lst, N]))
    return ans


a = lambda p: (p-2)/2
b = lambda p: -(p-4)/2

pgon = lambda p, n: int(a(p) * n**2 + b(p) * n)
# c sign is inverted
inverse = lambda p, c: (-b(p) + (b(p)**2 + 4 * a(p) * c)**(1/2))/(2*a(p))

_ = int(input())
P = sorted(map(int, input().split()), reverse=True)
lower_n = math.ceil(inverse(P[0], 1000))
upper_n = math.floor(inverse(P[0], 9999))
first = [pgon(P[0], n) for n in range(lower_n, upper_n+1)]

ans = set()
for f in first:
    for t in search_cycle(P[1:], [f]):
        if len(set(t)) == len(t):
            ans.add(sum(t))

for z in sorted(list(ans)):
    print(z)
