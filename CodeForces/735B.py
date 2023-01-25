a,b,c = [int(i) for i in input().strip().split(" ")]
l = [int(i) for i in input().strip().split(" ")]
l.sort()
sum1 = 0
for i in range(min(c,b)):
    sum1+=l.pop()
sum1 /= min(c,b)
sum2 = 0
for i in range(max(c,b)):
    sum2+=l.pop()
sum2/= max(c,b)
print(sum1+sum2)