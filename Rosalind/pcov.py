import sys

pre = {}
for line in sys.stdin:
    DNA = line.strip()
    pre[DNA[:-1]] = DNA

ans = DNA[-1]
DNA2 = pre[DNA[1:]]
while DNA2 != DNA:
    ans += DNA2[-1]
    DNA2 = pre[DNA2[1:]]
print(ans)