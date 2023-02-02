import math
days = 0
h1, h2 = map(int, input().split())
up, down = map(int, input().split())
net_day = up*12 - down*12

if h1 + up*8 >= h2:
    print(0)
elif net_day <= 0:
    print(-1)
else:
    h1 += up*8 - down*12
    print(1 + math.ceil((h2 - up*12 - h1)/net_day))