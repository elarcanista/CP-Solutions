def gcd(a, b):
    if b == 0:
        return a
    return lcm(b,a%b)

def lcm(l):
    temp = (l[0]*l[1])//gcd(l[0],l[1])
    for i in range(2, len(l)):
        temp = (temp*l[i])//gcd(temp, l[i])
    return temp

TC = int(input().strip())
for i in range(TC):
    n, k = [int(i) for i in input().strip().split(" ")]
    l = [int(i) for i in input().strip().split(" ")]
    if lcm(l) % k == 0:
        print("YES")
    else:
        print("NO")
